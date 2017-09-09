tree=[] #KRUSKALS ALGORITHM
wt={}
#input graph
n,e=map(int,input().split())
setofset=[]
for i in range(1,n+1):
	setofset.append([i])
def findset(u):
	global setofset
	for x in setofset:
		if u in x:
			return setofset.index(x)
def union(u,v):
	a=findset(u)
	b=findset(v) #REPRESENTATIVE RETURNED BY FINDSET IS THE INDEX OF SET IN SETOFSET
	global setofset
	setofset[a].extend(setofset[b])
	del setofset[b]
for i in range(e):
	a,b,w=map(int,input().split())
	wt[(a,b)]=w
# SORT THE EDGES BY WEIGHTS IN NON DECREASING ORDER AND STORE IN 'edges'	
l=list(wt.values())
l.sort()
edges=[]
for  i in l:
	x=[a for a in wt if wt[a]==i]
	del wt[x[0]]
	x=tuple(x[0])
	edges.append(x)
# SORTING ENDS!	
for x in edges:
	u,v=x
	if findset(u)!=findset(v):
		tree.append((u,v))
		union(u,v)
print(tree)
