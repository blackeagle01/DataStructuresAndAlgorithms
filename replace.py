def replace(string,replace):
 string=string.rstrip()
 try:
  x=string.rindex(" ")
 except:
  x=string.rindex(",")
 string=string[:x+1]+replace
 return string
 
print(replace(input(),input()))
