sum,n=map(int ,input().split())
c=[int(k) for k in input().split()]
d={}
def ways(sum):
 if sum in d:
   return d[sum]
 if sum<0:
   return 0
 if sum is 0:
   return 1
 k=0
 for i in range(n):
   k+=ways(sum-c[i])
   d[sum]=k
 return d[sum]
print(ways(sum))
