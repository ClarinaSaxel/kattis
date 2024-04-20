d={2:1/36,3:2/36,4:3/36,5:4/36,6:5/36,7:6/36}
n,p=int(input()),0
for h in input().split():p+=d[7-abs(int(h)-7)]
print(p)