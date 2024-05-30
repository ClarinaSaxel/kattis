I,r=input,''
n,m=[int(x)for x in I().split()]
s=[int(x)for x in I().split()]
l=set(s)&{int(x)for x in I().split()}
for e in s:
    if e in l:r+=f' {e}'
print(r[1:])