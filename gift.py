t=input()
for i in range(t)
 n=input() 
 n=int(n) 
 l=[i for i in range(1,n+1)]
 def deleven(l):
  l1=[]
  for i in range(len(l)):
   if i%2 is not 0:
    l1.append(i)
  l=[l[i] for i in l1]
  return l
 def delodd(l):
  l1=[]
  for i in range(len(l)):
   if i%2 is  0:
    l1.append(i)
  l=[l[i] for i in l1]
  return l
 while 1:
  l=deleven(l)
  if len(l) is 1:
   print(l[0])
   break
  l.reverse()
  l=deleven(l)
  l.reverse()
  if len(l) is 1:
   print(l[0])
   break

