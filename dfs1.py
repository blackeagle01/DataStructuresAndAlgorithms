n,m=map(int,input().split())
adj=[[] for i in range(n+1)]
visited=[]
current=0
def dfs_visit(node):
	print(node,end='\n')
	for x in adj[node]:
		if x not in visited:
		  visited.append(x)
		  dfs_visit(x)
		else:
		  return True	
		
def cycle():
	for x in range(1,n+1):
		if x not in visited:
			visited.append(x)
			global current
			current=x
			if dfs_visit(x):
				print('cycle')
for i in range(m):
	k,l=map(int,input().split())
	adj[k].append(l)
dfs()
if(cycle==1):
	print('cycle')




'''visited=[]
current=0
def dfs_visit(node):
	for x in adj[node]:
		if x==current:
			return True
		else:
			dfs_visit(x)

def cycle(adj):
	for x in range(1,n+1):
		global current
		current=x
		 if dfs_visit(x):
		 	return True
	return False
for i in range(m):
	k,l=map(int,input().split())
	adj[k].append(l)
if cycle(adj):
	print('cycle')
else:
	print('no cycle')'''