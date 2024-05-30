I=input
c,l,s=float(I()),int(I()),0
for _ in range(l):
    [w,l]=[float(x) for x in I().split()]
    s+=w*l*c
print(s)