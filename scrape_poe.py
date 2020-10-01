"""
SCRAPE POE POEMS.

Webscraper for downloading the poems of Edgar Allan Poe for text generation 
using GPT-2-simple from minimaxir's repo 
(https://github.com/minimaxir/gpt-2-simple).

Scraper uses Beautiful Soup for extracting texts from:

"""

import requests
import re
from bs4 import BeautifulSoup

base_url ='http://www.poetryloverspage.com/poets/poe/poe_ind.html'
req = requests.get(base_url)
soup = BeautifulSoup(req.content, 'html.parser')

poem_urls = soup.select("#display_poem_main a[href$='.html']")

href = []
for url in poem_urls:
    href.append(url.get('href'))
    
del href[-1] # Last URL not needed in list    

poems = []    
for url in href:
 
 
 
 
 
    # url = 'https://poestories.com{}'.format(url)
    # req = requests.get(url)
    # soup = BeautifulSoup(req.content, 'html.parser')
    # poems.append(soup.find('p', class_=lambda x: 'poem' in x or 'p2' in x).text.strip())
        

    
    

