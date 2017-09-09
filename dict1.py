from bs4 import *
import requests
string=input()
meanings=[]
def getmeaning(string):
 try:
  url="http://www.dictionary.com/browse/"+string+"?s=t"
  html=requests.get(url)
 except:
  pass
 bsobj=BeautifulSoup(html.content,"lxml")
 namelist=bsobj.find_all("div",{"class":"def-content"})
 for name in namelist:
  meanings.append(name.text)
 return meanings
meanings=getmeaning(string)
if len(meanings) is 0:
 meanings=getmeanings(correction(string))
print(meanings[0])

