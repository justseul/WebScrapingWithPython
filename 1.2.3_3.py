from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try: 
        bs = BeautifulSoup(html,'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("https://pythonscraping.com/pages/page1.html")
if title == None:
    print('title could not be found')
else:
    print(title)
