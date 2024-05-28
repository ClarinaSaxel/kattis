import math
[p,q,s]=[int(x)for x in input().split()]
print('no'if math.lcm(p,q)>s else'yes')