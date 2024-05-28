import math
i,I,l=int,input,[]
for _ in range(i(I())):
    s,r=I(),''
    q=i(math.sqrt(len(s)))
    for a in range(1,q+1):
        for b in range(1,q+1):
            r+=s[b*q-a]
    l+=[r]
print('\n'.join(l))