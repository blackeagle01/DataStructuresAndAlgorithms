n,m=map(int,input().split())
coins=list(map(int,input().split()))
d={}
def ways(n):
	if n in d:
		return d[n]
	elif n<0:
		return 0
	elif n==0:
		d[n]=1
		return d[n]
	else:
		summ=0
		for x in coins:
			summ+=ways(n-coins[x])
			d[n]=summ
			return d[n]

print(ways(n))