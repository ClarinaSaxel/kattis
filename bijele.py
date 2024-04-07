r,w=[1,1,2,2,2,8],[int(x)for x in input().split()]
print(' '.join(str(r[i]-w[i])for i in range(6)))