from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--disable-gpu")
#options.add_argument("--headless=new")

driver = webdriver.Chrome(
    service=Service('C:\Program Files (x86)\Google\chromedriver-win64\chromedriver.exe'),
    options=options
)

city = 'seattle'
state_abbreviation = 'wa'
driver.get(f'https://www.travelmath.com/cities-near/{city.capitalize()},+{state_abbreviation.upper()}')
    
html = driver.page_source

with open('test.html', 'w', encoding='utf-8') as f:
    f.write(html)

driver.quit()