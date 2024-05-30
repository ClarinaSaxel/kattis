I,L=input,[]
for _ in range(int(I())):
    s,t=I(),I()
    L.append(s+'\n'+t+'\n'+''.join(a for a in ["." if s[i]==t[i] else "*" for i in range(len(s))])+'\n')
for i in L: print(i)