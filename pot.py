I=input
s=0
for _ in range(int(I())):
    l=I()
    s+=int(l[:-1])**int(l[-1])
print(s)