[n,m]=[int(x)for x in input().split()]
k=[0 for x in range(n+m-1)]
for i in range(n):
    for j in range(m):k[i+j]+=1
for e in range(len(k)):
    if k[e]==max(k):print(e+2)