i,I,r=int,input,[]
for _ in range(i(I())):
    l=[i(x) for x in I().split()]
    s=0
    for e in range(len(l)-1):
        s+=max(l[e+1]-l[e]*2,0)
    r.append(str(s))
print('\n'.join(r))