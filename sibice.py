import math
I=input
[n,w,h]=[int(x) for x in I().split()]
a=math.hypot(w,h)
for i in range(n):
    print('DA'if int(I())<=a else'NE')