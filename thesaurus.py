from bs4 import BeautifulSoup
import requests
string=input("enter word")
url="http://www.thesaurus.com/browse/"+string
html=requests.get(url)
bs=BeautifulSoup(html.content,"lxml")
namelist=bs.find_all("a",{"class":"common-word"})
for name in namelist:
	new=name.text
	new=new.rstrip()
	new=new[:-4]
	if new.isspace(): continue
	print(new)

	