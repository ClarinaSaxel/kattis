g,d,e=[],'',''
for _ in range(3):
    g.append(input())
for i in range(3):
    s=''
    d+=g[i][i]
    e+=g[i][2-i]
    for j in range(3):
        s+=g[j][i]
    g.append(s)
g.append(d)
g.append(e)
print('Jebb' if 'OOO' in g else 'Neibb')