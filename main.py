from selenium import webdriver as wd
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = wd.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)

url = "https://hotcopper.com.au/announcements/asx/?favs=No&price_sensitive=Any&summary=Change+of+Director%27s+Interest+Notice&exchange=1"

driver.get(url)

page_source = driver.page_source

soup = BeautifulSoup(driver.page_source, 'html.parser')

results = soup.find("table", {"class": "table is-fullwidth is-hidden-touch"})
print(results.text)