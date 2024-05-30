[n,h,v]=[int(i) for i in input().split()]
print(max(h*v,(n-h)*(n-v),h*(n-v),v*(n-h))*4)