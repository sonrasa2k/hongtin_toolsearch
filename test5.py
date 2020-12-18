#importing the libraries we will need
import pandas as pd
import numpy as np
import urllib
from fake_useragent import UserAgent
import requests
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
def google_results(keyword, n_results):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }
    query = keyword
    query = urllib.parse.quote_plus(query) # Format into URL encoding
    number_result = n_results
    ua = UserAgent()
    google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
    response = requests.get(google_url, headers = headers)
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup)
    result = soup.find_all('div', attrs = {'class': 'ZINbbc'})
    results=[re.search('\/url\?q\=(.*)\&sa',str(i.find('a', href = True)['href'])) for i in result]
    links=[i.group(1) for i in results if i != None]
    return (links)

link = google_results('machine learning in python', 10)
print(link)