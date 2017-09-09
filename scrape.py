import requests
from bs4 import BeautifulSoup
starturl="http://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html"
urls=[]
html=requests.get(starturl)
bs=BeautifulSoup(html.content,"lxml")
namelist=bs.find_all("a")
for name in namelist:
 if 'href' in name.attrs:
  urls.append(name.text)
  
print(urls)
