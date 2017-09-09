from bs4 import *
import requests
#from spellcheck import correction
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
 fo=open("foo.txt","w")
 i=1
 for name in namelist:
  x=str(i)
  fo.write(x+name.text)
  meanings.append(name.text)
  i+=1
meanings=getmeaning(string)
'''if(len(meanings)==0):
 string=correction(string)
 meanings=getmeanings(string)'''
print(meanings[0])
