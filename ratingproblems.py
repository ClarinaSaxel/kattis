I=input
[n,k],s=[int(x) for x in I().split()],0
for _ in range(k):
    s+=int(I())
print(f'{(s+(n-k)*(-3))/n} {(s+(n-k)*(3))/n}')