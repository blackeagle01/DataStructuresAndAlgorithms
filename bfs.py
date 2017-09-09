n,m=map(int,input().split())
adj=[[] for i in range(n+1)]
for i in range(m):
	a,b=map(int,input().split())
	adj[a].append(b)
queue=[1]
visited=[]
count={1:0}
parent={1:-1}
def dist(parent,node):
	c=0
	while parent[node]!=-1:
		node=parent[node]
		c+=1
	return c
while queue!=[]:
	x=queue[0]
	del queue[0]
	visited.append(x)
	for i in adj[x]:
		if i not in visited and i not in queue:	
			parent[i]=x
			queue.append(i)
for i in range(n):
	count[i]=dist(parent,i)
print(count)
