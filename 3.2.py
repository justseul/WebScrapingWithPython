from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import re

pages = set()

def getLinks(pageUrl):
    global pages
    try:
        html = urlopen(f'http://en.wikipedia.org{pageUrl}')
        bs = BeautifulSoup(html,'html.parser')
        for link in bs.findAll('a', href=re.compile('^(/wiki/)')):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    newPage = link.attrs['href']
                    print(newPage)
                    pages.add(newPage)
                    getLinks(newPage)
    except HTTPError as e:
        return None

getLinks('')