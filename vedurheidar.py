I=input
w,r,s=int(I()),int(I()),''
for _ in range(r):
    [l,o]=I().split()
    s+=f'{l} lokud\n'if int(o)<w else f'{l} opin\n'
print(s[:-1])