n,m=map(int,input().split())
adj=[[] for i in range(n+1)]
wt={}
for i in range(m):
	a,b,w=map(int,input().split())
	adj[a].append(b)
	wt[(a,b)]=w
ds=[100000,0]+[1000 for i in range(n-1)]
q=[i for i in range(1,n+1)]
def extractmin(q):
	x=ds.index(min(ds))
	q.remove(x)
	return x,q
def relax(u,v):
	if ds[v]>ds[u]+wt[(u,v)]:
		ds[v]=ds[u]+wt[(u,v)]
	return ds
while q!=[]:
	u,q=extractmin(q)
	for v in adj[u]:
		ds=relax(u,v)
print([ds[i] for i in range(1,n+1)])