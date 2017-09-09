
n,e=map(int,input().split())
adlist=[[] for i in range(n+1)]
for i in range(e):
	a,b=map(int,input().split())
	adlist[a].append(b)
color={}
for i in range(n+1):
	color[i]='white'
def dfs():
	for i in range(1,n+1):
		if color[i]=='white':
			visit(i)
flag=0
def visit(i):
	color[i]='gray'
	for j in adlist[i]:
		if color[j]=='white':
			visit(j)
		elif color[j]=='gray':
			global flag
			flag=1
	color[i]='black'
dfs()
if flag==1:
	print('cycle')
else:
	print("no cycle")