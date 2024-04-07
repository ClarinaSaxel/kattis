I=input
for i in range(int(I())):
    [k,n]=[int(x)for x in I().split()]
    print(k,int((n*(n+1))/2+n))