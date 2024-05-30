[l,r]=[int(x) for x in input().split()]
s=2*max(l,r)
print('Not a moose' if s==0 else f'Odd {s}' if l!=r else f'Even {s}')