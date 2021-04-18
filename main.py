from selenium import webdriver as wd
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

driver = wd.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
url = "https://hotcopper.com.au/announcements/asx/?favs=No&price_sensitive=Any&summary=Change+of+Director%27s+Interest+Notice&exchange=1"
driver.get(url)
page_source = driver.page_source

def convertPagetoPandas(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    soupResults = soup.find("table", {"class": "table is-fullwidth is-hidden-touch"})
    items = soupResults.findAll("tr")
    rows = []
    for item in items:
        tickerElement = item.find("span", {"class": "stock-pill"})
        dateElement = item.find("td", {"class": "stats-td"})
        linksElement = item.find_all("td", {"class": "stats-td"})
        if not (tickerElement or dateElement or linksElement):
            continue
        tickerText = tickerElement.text
        dateText = dateElement.text
        downloadText = linksElement[1].find('a', href=True).get('href')
        row = [tickerText, dateText, downloadText]
        rows.append(row)
    df = pd.DataFrame.from_records(rows, columns=["Ticker", "Ann_Date", "url"])
    return df


# convertPagetoPandas(page_source).to_csv("test", sep='\t')