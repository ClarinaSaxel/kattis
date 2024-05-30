[h,m]=[int(x) for x in input().split()]
t=h*60+m-45
print((t//60)%24,t%60)