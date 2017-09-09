t=int(input())
for x in range(t):
 n=int(input())
 l=[int(k) for k in input().split()]
 d=[[-100000 for i in range(n)] for i in range(n)]
 for i in range(n):
  for j in range(i,n):
    if i is j:
      d[i][j]=l[j]
    else:
      d[i][j]=d[i][j-1]+l[j]
 a=max(l)
 for i in l:
   if(i>0):
     a=sum([i for i in l if i>0])
 b=max(list(map(max,[d[i] for i in range(n)])))
 print(b,a,end="\n")

