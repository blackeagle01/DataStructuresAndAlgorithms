def edit(string):
 string=string.rstrip()
 try:
  x=string.rindex(",")
  newstr=string[x+1:]
 except:
   try:
    x=string.rindex(" ")
    newstr=string[x+1:]
   except: pass
   try: 
    x=string.rindex("(")
    newstr=string[x+1:-1]
   except: pass
 return newstr
string=edit(input())
print(string)
