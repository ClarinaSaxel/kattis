n=int(input())
a,c='+','|'
s=a+n*'-'+a
print(s)
for _ in range(n):
    print(c+n*' '+c)
print(s)