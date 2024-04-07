I=input
m,n,c=int(I()),int(I()),0
for _ in range(n):c+=I().count('.')
print(c/(m*n))