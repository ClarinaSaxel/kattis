n,c=int(input()),0
l=[int(x) for x in input().split()]
a=l.copy()
a.sort()
for i in range(n):
    if a[i]!=l[i]:
        c+=1
print(c)