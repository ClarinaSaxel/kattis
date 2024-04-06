i,I=int,input
[r,n]=[i(x)for x in I().split()]
l=list(range(1,r+1))
for _ in range(n):
    l.remove(i(I()))
print('too late'if r==n else l[0])