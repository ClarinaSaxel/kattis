from math import ceil
[a,i]=[int(x) for x in input().split()]
for e in range(a*(i-1)-1,a*i+1):
    if ceil(e/a)==i:print(e);break