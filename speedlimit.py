I,i,j=input,int,[]
r=i(I())
while r>-1:
    g,h=0,0
    for _ in range(r):
        [s,t]=[i(x) for x in I().split()]
        g+=s*(t-h)
        h=t
    j.append(f'{g} miles')
    r=i(I())
print('\n'.join(j))