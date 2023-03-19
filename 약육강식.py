n=int(input())
sharks=list(map(int,input().split()))
prefix=[1 for i in range(n)]

for i in range(1,n):
	for j in range(0,i):
		if sharks[j]<sharks[i]):
			prefix[i]=max(prefix[i],prefix[j]+1)

answer=max(prefix)

print(answer)
