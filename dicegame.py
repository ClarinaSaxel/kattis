g=sum(int(x) for x in input().split())
e=sum(int(x) for x in input().split())
print('Gunnar' if g>e else 'Emma'if e>g else 'Tie')