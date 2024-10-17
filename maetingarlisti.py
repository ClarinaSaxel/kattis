n,r,c=[int(x) for x in input().split()]
s,a=[],[]
for _ in range(r):
    s.append(input().split())
for i in range(r):
    l=[]
    for _ in range(c):
        l.append(input())
    a.append('left') if l==s[i] else a.append('right')
print('\n'.join(a))