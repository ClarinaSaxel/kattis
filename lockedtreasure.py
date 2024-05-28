import math
I=input
for _ in range(int(I())):
    [n,m]=[int(x) for x in I().split()]
    print(math.comb(n,m-1))