s=input()
r=s[0]
for l in s:
    if l!=r[-1]:r+=l
print(r)