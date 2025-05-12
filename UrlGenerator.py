import json
import urllib.parse

import requests
from bs4 import BeautifulSoup

def url_generator():
    pass

def get_nearby_cities(city: str, state_abbreviation:str):
    url = f'https://www.travelmath.com/cities-near/{city.capitalize()},+{state_abbreviation.upper()}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    related_list = soup.find('ul', class_='related')
    city_links = related_list.find_all('a')
    return [link.text.strip() for link in city_links]

