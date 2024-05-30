I,s,r=input,0,'possible'
for _ in range(int(I())):
    [g,b]=[int(x) for x in I().split()]
    s+=g
    if s<b and r[0]=='p':r='im'+r
print(r)