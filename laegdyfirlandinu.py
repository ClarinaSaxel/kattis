[n,m]=[int(x) for x in input().split()]
l=[]
for _ in range(n):
    l.append([int(x) for x in input().split()])
for i in range(1,n-1):
    for j in range(1,m-1):
        if l[i][j]<min(l[i-1][j],l[i][j+1],l[i+1][j],l[i][j-1]):
            print("Jebb")
            exit()
print("Neibb")