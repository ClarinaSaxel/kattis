I,c,d=input,0,0
l,x=[int(a) for a in I().split()]
for _ in range(x):
    s=I().split()
    if s[0]=='enter' and c+int(s[1])>l:
        d+=1
    elif s[0]=='enter':
        c+=int(s[1])
    else:
        c-=int(s[1])
print(d)