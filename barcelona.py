[n,k]=[int(x) for x in input().split()]
l=[int(x) for x in input().split()]
s='' if k==l[0] else 'naest' if k==l[1] else f'{l.index(k)+1} '
print(s+'fyrst')