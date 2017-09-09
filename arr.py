a,b=map(int,input().split())
l=[int(n) for n in input().split()]
l1=[]
for i in range(b):
 c,d=map(int,input().split())
 l1.append(sum(l[c-1:d]))
for i in l1:
 print(i,"\n")
 
