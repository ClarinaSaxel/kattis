i,r,l=input(),[],[':)',';)',':-)',';-)']
for j in range(4):
    for _ in range(i.count(l[j])):
        a=i.index(l[j])
        r.append(str(a))
        i=i[:a]+'n'+i[a+1:]
print('\n'.join(r))