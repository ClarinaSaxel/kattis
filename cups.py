d={}
for _ in range(int(input())):
    l=input().split()
    if l[0].isnumeric():
        d[int(l[0])//2]=l[1]
    else:
        d[int(l[1])]=l[0]
while d.keys():
    m=min(d.keys())
    print(d[m])
    d.pop(m)