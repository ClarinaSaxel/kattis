I,d,s=input,{},''
n,l=int(I()),I().split()
for _ in range(int(I())):
    a,b=I().split()
    d[a]=b
for i in range(n):
    s+=d[l[i]]+' '
print(s)