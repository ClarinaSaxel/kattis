I=input
k,m,f=int(I()),I(),I()
n=len(m)
l=len([i for i in range(n) if m[i]==f[i]])
print(n-max(k,l)+min(k,l))