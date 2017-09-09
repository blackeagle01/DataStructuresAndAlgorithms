import requests
from bs4 import *
print("Enter search")
s=input()
url="https://en.wikipedia.org/wiki/"+s
html=requests.get(url)
bs=BeautifulSoup(html.content,"lxml")
namelist=bs.find_all("p")
for name in namelist:
 print(name.text)
