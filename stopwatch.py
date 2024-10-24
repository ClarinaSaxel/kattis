I=input
N,r=int(I()),0
for _ in range(N//2):
    a,b=int(I()),int(I())
    r+=b-a
print('still running' if N%2==1 else r)