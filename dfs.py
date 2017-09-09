n,e=map(int,input().split())
adj=[[] for i in range(n+1)]
for i in range(e):
	a,b=map(int,input().split())
	adj[a].append(b)
adjtr=[[] for i in range(n+1)]
for i in range(1,n+1):
	for j in adj[i]:
		adjtr[j].append(i)
color={}
for i in range(1,n+1):
	color[i]='white'
time=0
start,finish={},{}
def dfs():
	for i in range(1,n+1):
		if color[i]=='white':
			visit(i)
cycle=0
topo=[]
def dfsgt():
	global topo
	global adjtr
	for i in topo:
		if color[i]=='white':
			visit(i,adjtr)

def visit(u,adj):
	global color
	global time
	time+=1
	start[u]=time
	color[u]='gray'
	for i in adj[u]:
		if color[i]=='white':
			visit(i)
		elif color[i]=='gray':
			global cycle
			cycle+=1
	color[u]='black'
	global topo
	topo.insert(0,u)
	time+=1
	finish[u]=time
dfs()
print(topo)
print(start,finish)
