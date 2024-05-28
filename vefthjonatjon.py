I=input
k=[0,0,0]
for _ in range(int(I())):
    l=[1 if x=='J' else 0 for x in I().split()]
    k=[sum(x) for x in zip(k,l)]
print(min(k))