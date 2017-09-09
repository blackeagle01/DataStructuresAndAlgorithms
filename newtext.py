def get_last_word(string):
 string=string.rstrip()
 if string.endswith(".") or string.endswith(","):
  string=string[:-1]
 l=list(string)
 if not "," in l:
  if not " " in l:
   return string
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
 return newstr.lstrip()
print(get_last_word(input()))
