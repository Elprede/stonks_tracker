from selenium import webdriver as wd
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = wd.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

def scrapeTickerId():
    tag_id = 287
    while tag_id < 289:
        url = f"https://hotcopper.com.au/announcements/asx/?favs=No&price_sensitive=Any&tag_id={tag_id}&exchange=1"
        driver.get(url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        soupResults = soup.find("table", {"class": "table is-fullwidth is-hidden-touch"})
        tickerElement = soupResults.find("a", {"class": "tag-type-symbol"})
        tickerText= tickerElement.text
        print(tag_id, tickerText)

        # test


        tag_id += 1

    driver.quit()

scrapeTickerId()