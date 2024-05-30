I,m=input,[]
l,d,x=int(I()),int(I()),int(I())
for i in range(l,d+1):
    if sum([int(e) for e in str(i)])==x:m.append(i)
print(f'{m[0]}\n{m[-1]}')