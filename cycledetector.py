n,m=map(int,input().split())
adj=[[] for i in range(n+1)]
for i in range(m):
	k,l=map(int,input().split())
	adj[k].append(l)
visited=[]
l=[]
def dfs():
	for i in range(1,n+1):
		count=0;max=0;
		if i not in visited:
			visit(i,count)
			


def visit(node,count):
	visited.append(node)
	count+=1
	print(node)
	for i in adj[node]:
		if i not in visited:
			visit(i,count)
	global l
	l.append(count)

dfs()
print(max(l))



	
