i,I,t=int,input,[]
[n,d]=[i(x) for x in I().split()]
while d>0:
    s=f'{n//d} {n%d} / {d}'
    t+=[s]
    [n,d]=[i(x) for x in I().split()]
print('\n'.join(t))