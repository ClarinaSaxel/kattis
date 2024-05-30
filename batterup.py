i,I=int,input
n=i(I())
l=[i(x) for x in I().split()]
for e in l:
    if e<0:n-=1
l=[e for e in l if e>0]
print(sum(l)/n)