a,b=map(int,input().split())
q=[a]
x=q[0]
p={a:-1}
while x!=b:
	x=q[0]
	del q[0]
	if x*2 not in p:
		q.append(x*2)
		p[x*2]=x
	if x-1 not in p:
		q.append(x-1)
		p[x-1]=x
count=0	
l=[]
while p[x]!=-1:
	l.append(x)
	x=p[x]
	count+=1
l.append(a)
l=l[::-1]
for i in l:
	print(i,'-->',end='')
print('\n')
print('count=',count)
