l=list(map(int,input().split()))
l.insert(0,0)
initial=[]
for i in range(3):
      initial.append([])
      for j in range(3):
            initial[i].append(l[0])
            l=l[1:]
def getposition(initial):
      for i in range(3):
            for j in range(3):
                  if initial[i][j]==0:
                        return (i,j)
def getstate(initial,t,u):
      a,b=t
      c,d=u
      x=initial[a][b]
      initial[a][b]=initial[c][d]
      initial[c][d]=x
      return initial
def ingrid(a,b):
      if a in range(0,2) and b in range(0,2):
            return True
      else:
            return False
def genstates(initial,visited):
      x,y=getposition(initial)
      states=[]
      if ingrid(x,y+1):
            newstate=getstate(initial,(x,y+1),(x,y))
            if newstate not in visited:
                  states.append(newstate)
                  
      if ingrid(x,y-1):
            newstate=getstate(initial,(x,y-1),(x,y))
            if newstate not in visited:
                  states.append(newstate)
                  
      if ingrid(x+1,y):
            newstate=getstate(initial,(x+1,y),(x,y))
            if newstate not in visited:
                  states.append(newstate)
                  
      
      if ingrid(x-1,y):
            newstate=getstate(initial,(x-1,y),(x,y))
            if newstate not in visited:
                  states.append(newstate)
                  
      return states,visited
states=[]
visited=[]
states,visited=genstates(initial,visited)          
print(states)       

 
