n,m=map(int,input().split())
adj=[[] for i in range(n)]
for i in range(n):
	adj[i].extend(list(map(int,input().split())))
d={}
def fillup(t):
	a,b=t
	l=[]
	for i in range(3):
		x=a-1+i
		for j in range(3):
			y=b-1+j
			if (x,y)==(a,b):
				continue
			if x in range(n) and y in range(m):
				if adj[x][y]==1:
					l.append((x,y))
	return l	
for i in range(n):
	for  j in range(m):
		if adj[i][j]==1:
			d[(i,j)]=fillup((i,j))
count=[]
visited=[]
c=0
def visit(node):
	global c
	c+=1
	visited.append(node)
	for x in d[node]:
		if x not in visited:
			visit(x)
	global count
	count.append(c)
		
def dfs():
	for x in d.keys():
		global c
		c=0
		if x not in visited:
			visit(x)
dfs()
print(max(count))