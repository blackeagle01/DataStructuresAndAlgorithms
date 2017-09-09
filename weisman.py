n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
q=int(input())
qarr=[]
for i in range(q):
	qarr.append(list(map(int,input().split())))
d={}
for i in range(1,n+1):
	for j in range(i,n+1):
		if i==j:
			d[(i,j)]=arr[i]
		else:
			d[(i,j)]=d[(i,j-1)]*arr[j]
'''def prod(i,j):
	pr=1
	if (i,j) in d:
	 	return d[(i,j)]
	elif i==j:
	 	d[(i,j)]=arr[i]
	 	return d[(i,j)]
	else:
		pr=arr[i]*prod(i+1,j)
		d[(i,j)]=pr
		return d[(i,j)]
'''
def prod(i,j):
	return d[(i,j)]
for i in qarr:
	print(prod(i[0],i[1])%i[2])

