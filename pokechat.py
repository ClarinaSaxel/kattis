I=input
s,l,r=I(),I(),''
for i in range(len(l)//3):
    r+=s[int(l[i*3:i*3+3])-1]
print(r)
