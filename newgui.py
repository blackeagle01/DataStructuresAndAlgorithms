adj=[]
for i in range(1000):
 adj.append([])
 for j in range(1000):
  adj[i].append(0)
def ans(m,n):
 if adj[m][n] is not 0:
  return adj[m][n]
 elif m is 0 or n is 0:
  adj[m][n]=1
  return adj[m][n]
 else:
  adj[m][n]=ans(m-1,n)+ans(m,n-1)
  return adj[m][n]
print(ans(int(input()),int(input())))

