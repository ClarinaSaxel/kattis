from math import sqrt
i,j,c=int(input()),1,0
while i-j>=0:
    i-=j
    j=(int(sqrt(j))+2)**2
    c+=1
print(c)