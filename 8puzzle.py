inp=list(map(int,input().split()))
initial=[[] for i in range(3)]
goal=[[0,1,2],[3,4,5],[6,7,8]]
for i in range(3):
	for j in range(3):
		initial[i].append(inp[0])
		inp=inp[1:]
def swap(new,u,v):
	a,b=u
	c,d=v
	t=new[a][b]
	new[a][b]=new[c][d]
	new[c][d]=t
	return new
def ingrid(a,b):
	if a in range(0,3) and b in range(0,3):
		return True
	else:
		return False
def position(state):
	for i in range(3):
		for j in range(3):
			if state[i][j]==0:
				return (i,j)
def neighbours(state,visited):
	  x,y=position(state)
	  final=[]
	  if ingrid(x+1,y):
	  	newstate=state.copy()
	  	newstate=swap(newstate,(x+1,y),(x,y))
	  	if newstate not in visited:
	  		final.append(newstate)
	  if ingrid(x-1,y):
	  	newstate=state.copy()
	  	newstate=swap(newstate,(x-1,y),(x,y))
	  	if newstate not in visited:
	  		final.append(newstate)
	  if ingrid(x,y+1):
	  	newstate=state.copy()
	  	newstate=swap(newstate,(x,y+1),(x,y))
	  	if newstate not in visited:
	  		final.append(newstate)
	  if ingrid(x,y-1):
	  	newstate=state.copy()
	  	newstate=swap(newstate,(x,y-1),(x,y))
	  	if newstate not in visited:
	  		final.append(newstate)
	  return final
q=[initial]
state=initial
visited=[initial]
print(visited)
parent={}
x,y=position(state)
final=[]
print(ingrid(x+1,y))
if ingrid(x+1,y):
	newstate=state
	newstate=swap(newstate,(x+1,y),(x,y))
	print(newstate)
	print(visited)
	print(newstate not in visited)
	if newstate not in visited:
		final.append(newstate)
'''if ingrid(x-1,y):
	newstate=state.copy()
	newstate=swap(newstate,(x-1,y),(x,y))
	if newstate not in visited:
		final.append(newstate)
if ingrid(x,y+1):
	newstate=state.copy()
	newstate=swap(newstate,(x,y+1),(x,y))
	if newstate not in visited:
		final.append(newstate)
if ingrid(x,y-1):
	newstate=state.copy()
	newstate=swap(newstate,(x,y-1),(x,y))
	if newstate not in visited:
		final.append(newstate)'''
print(final)
'''while True:
	x=q[0]
	del q[0]
	if x==goal:
		break
	else:
		visited.append(x)
		q.extend(neighbours(x,visited))
print(x)'''









