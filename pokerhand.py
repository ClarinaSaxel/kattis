l=[x[0] for x in input().split()]
s,d=set(l),{}
for e in s:
    d[e]=0
for e in l:
    d[e]+=1
print(max(d.values()))