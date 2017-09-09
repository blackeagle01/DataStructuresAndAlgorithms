n,m=[int(k) for k in input().split()]
shots=[[] for i in range(n)]
player=[[] for i in range(m)]
for i in range(n):
    shots[i]=[int(k) for k in input().split()]
for i in range(m):
    player[i]=[int(k) for k in input().split()]
st=[0 for i in range(m)]
print(shots,player)
'''for i in range(m):
    for j in range(n):
        if ((player[i][0]>=shots[j][0] and player[i][1]<=shots[j][1])) or ((player[i][1]>=shots[j][0] and player[i][1]<=shots[j][1])):
            st[i]+=1
print(sum(st))'''
