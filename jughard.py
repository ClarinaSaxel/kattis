import math
I=input
for i in range(int(I())):
    [a,b,d]=[int(x) for x in I().split()]
    print('Yes'if d%math.gcd(a,b)==0else'No')