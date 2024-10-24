I,r=input,[]
n,p,s=[int(x) for x in I().split()]
for _ in range(s):
    l=[int(x) for x in I().split()][1:]
    r.append('KEEP' if p in l else 'REMOVE')
print('\n'.join(r))