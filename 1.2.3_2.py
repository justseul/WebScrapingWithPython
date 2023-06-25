from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

html = urlopen("https://pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html,'html.parser')
try: 
    badContent = bs.nonExistingTag.anotherTag
except AttributeError as e:
    print("tag was not found")
else:
    if badContent == None:
        print("tag was not found")
    else:
        print(badContent)