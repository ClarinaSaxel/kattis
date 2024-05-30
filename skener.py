I,l,s=input,'',''
[r,c,y,z]=[int(x) for x in I().split()]
for _ in range(r):
    for j in I():
        l+=z*j
    for _ in range(y):
        s+=l+'\n'
    l=''
print(s)