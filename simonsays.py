I,r=input,''
for _ in range(int(I())):
    s=I()
    if s.startswith('Simon says '):r+=s[11:]+'\n'
print(r[:-1])