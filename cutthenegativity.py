I,s=input,''
for i in range(int(I())):
    l=[int(x) for x in I().split()]
    for j in range(len(l)):
        if l[j]!=-1:
            s+=f'\n{i+1} {j+1} {l[j]}'
print(str(s.count('\n'))+s)