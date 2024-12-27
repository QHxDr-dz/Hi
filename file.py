import bs4
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
x={"q":input("enter ur name you want to search about it" )}
z=urllib.parse.urlencode(x)
url='https://www.google.com/search'
url1=url+"?"+z
w=urllib.request.urlopen(url1)
#print(w.read(10000))
soup=BeautifulSoup(w,"html.parser")
for i in soup.find_all("h3"):
    print(i.text)