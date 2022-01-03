
"""The module searches for information about upcoming events on the page and outputs it to the console"""

import requests
from bs4 import BeautifulSoup

URL = 'https://www.python.org/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')

# Search for a block of information about upcoming events
block_info = soup.find('div', class_='medium-widget event-widget last')

# Event search in the block
events = block_info.find('ul', class_='menu')


for event in events:
    print(event.text.lstrip())
