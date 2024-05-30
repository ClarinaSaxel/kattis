I,c=input,0
[n,k,d]=[int(x) for x in I().split()]
for _ in range(n):
    s=int(I())
    if d+k-s>=14:c+=1
print(c)