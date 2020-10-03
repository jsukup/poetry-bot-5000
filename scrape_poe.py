"""
SCRAPE POE POEMS.

Webscraper for downloading the poems of Edgar Allan Poe for text generation 
using GPT-2-simple from minimaxir's repo 
(https://github.com/minimaxir/gpt-2-simple).

Scraper uses Beautiful Soup for extracting poems from:
http://www.poetryloverspage.com/poets/poe/poe_ind.html

"""

import requests
import re
from bs4 import BeautifulSoup
import csv

base_url ='http://www.poetryloverspage.com/poets/poe/poe_ind.html'
req = requests.get(base_url)
soup = BeautifulSoup(req.content, 'html.parser')

# Extract tags for each poem URL
poem_urls = soup.select("#display_poem_main a[href$='.html']")

# Keep only href
href = []
for url in poem_urls:
    href.append(url.get('href'))
    
del href[-1] # Last URL not needed in list    

# Scrape each poem from each href
poems = []    
for url in href:
    url = 'http://www.poetryloverspage.com/poets/poe/{}'.format(url)
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    poem = soup.select_one('#display_poem_main pre')
    poems.append(poem.text
                 .strip()
                 .replace('\n','')
                 .replace('\\','')
                 .replace('-',''))

# Save to columnar CSV file    
with open('poe.csv', 'w', newline='') as f:
    file = csv.writer(f)
    for poem in poems:
         file.writerow([poem])