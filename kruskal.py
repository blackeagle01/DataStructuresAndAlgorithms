n,m=map(int,input().split())
adj=[[] for i in range(n+1)]
newadj=adj.copy()
visited=[]
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


wt={}
for i in range(m):
	l=[]
	l=list(map(int,input().split()))
	adj[l[0]].append(l[1])
	wt[(l[0],l[1])]=l[2]
print(adj,wt,sep='\n')
edgewts=list(wt.values())
edgewts.sort()
added=[]
minwt=0
for i in edgewts:
    if len(added)==n:
    	break
	k,m=[x for x in wt if wt[x]==i]
	newadj[k].append(m)
	if k not in added:
		added.append(k)
	if m not in added:
		added.append(m)
	minwt+=i
	if  cycle(newadj):
		newadj[k].remove(m)
		minwt-=i
		added.remove(k)
		added.remove(m)
print(minwt)
	





