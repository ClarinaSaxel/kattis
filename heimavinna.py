i,l=int,[x for x in input().split(';')]
for e in range(len(l)):
    s=l[e].find('-')
    match s:
        case -1:l[e]=1
        case _:l[e]=i(l[e][s+1:])-i(l[e][:s])+1
print(sum(l))