import requests
from bs4 import BeautifulSoup

city = 'seattle'
state_abbreviation = 'wa'
url = f'https://www.travelmath.com/cities-near/{city.capitalize()},+{state_abbreviation.upper()}'

headers = {'User-Agent': 'Mozilla/5.0'}
resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')

# Find the section containing all cities
related_list = soup.find('ul', class_='related')


city_links = related_list.find_all('a')

for link in city_links:
    city_name = link.text.strip()
    city_url = f"https://www.travelmath.com{link['href']}"
    print(f"{city_name}: {city_url}")