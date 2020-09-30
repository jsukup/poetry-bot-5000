"""
SCRAPE POE POEMS.

Webscraper for downloading the poems of Edgar Allan Poe for text generation 
using GPT-2-simple from minimaxir's repo 
(https://github.com/minimaxir/gpt-2-simple).

General format of API requests from poetrydb 
(https://github.com/thundercomb/poetrydb):

/<input field>/<search term>[;<search term>][..][:<search type>]
[/<output field>][,<output field>][..][.<format>]
"""

import requests

response = requests.get('https://poetrydb.org/author/poe/author')