from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
service=Service('C:\Program Files (x86)\Google\chromedriver-win64\chromedriver.exe')

# Returns the list of lists for every listing that was found within these parameters at this site.
def get_available_listing_data(site: str, city:str, section:str, state:str, max_price:str, min_bedrooms:int, min_sq_ft: int):
    assert site.lower() in ['redfin', 'apartments.com', 'realtor.com', 'zillow'], "This is not one of the four legal sites"
    assert(min_bedrooms >= 0), "Must be real number of bedrooms (0 for studio)"
    assert(min_sq_ft >= 0), "Must be real number of sq ft"
    driver = webdriver.Chrome(
        service=Service('C:\Program Files (x86)\Google\chromedriver-win64\chromedriver.exe'),
        options=options
    )
    if site.lower() == 'redfin':
        url = ''
    elif site.lower() == 'apartments.com':
        url = ''
    elif site.lower() == 'realtor.com':
        url = ''
    elif site.lower() == 'zillow':
        url = ''


# Accepts the driver pointer and the url it is supposed to scrape and returns the raw html.
def scrape_url(driver: webdriver, url):
    driver.get(url)
    return driver.page_source

# Accepts the raw html of the location search and parses it to return a list of additional links that need scraping.
def locate_embedded_url(html):
    pass

# Accepts the raw html for a house/apartment and extracts Address, Name, Price, Sq footage, amenities
def extract_housing_informtation(html):
    pass

    