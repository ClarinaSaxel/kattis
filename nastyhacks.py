I=input
for _ in range(int(I())):
    [r,e,c]=[int(x) for x in I().split()]
    print('advertise' if e-c>r else'do not advertise' if e-c<r else'does not matter')