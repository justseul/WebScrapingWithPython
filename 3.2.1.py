from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen(f'http://en.wikipedia.org{pageUrl}')
    bs = BeautifulSoup(html,'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id = 'mw-content-text').findAll('p')[0])
        print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! Mo worries though!')
    except HTTPError as e:
        return None
    for link in bs.findAll('a',href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('--------------\n'+newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks('')