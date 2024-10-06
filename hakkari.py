[n,m]=[int(x) for x in input().split()]
c,k=0,[]
for i in range(n):
    l=input()
    for j in range(m):
        if l[j]=='*':
            c+=1
            k.append((i+1,j+1))
print(c)
for e in k:
    print(f'{e[0]} {e[1]}')