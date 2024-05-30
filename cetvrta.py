m,l=[],[]
for _ in range(3):
    r,s=[int(x) for x in input().split()]
    m.append(r) if m.count(r)<1 else m.remove(r)
    l.append(s) if l.count(s)<1 else l.remove(s)
print(m[0],l[0])