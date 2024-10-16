i=input()
s=i[0]
for j in range(1, len(i)):
    if i[j]!=i[j-1]:
        s+=i[j]
print(s)
    