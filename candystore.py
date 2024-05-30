I,l,m,t=input,[],[],[]
[n,q]=[int(x) for x in I().split()]
for _ in range(n):
    r=I()
    l.append(r)
    m.append(''.join([x[0] for x in r.split()]))
for _ in range(q):
    s=I()
    t.append('nobody' if s not in m else 'ambiguous' if m.count(s)>1 else l[m.index(s)])
print('\n'.join(t))