I,i=input,0
for _ in range(int(I())):
    c=I().lower()
    if 'rose' in c or 'pink' in c:i+=1
print(i if i>0 else 'I must watch Star Wars with my daughter')