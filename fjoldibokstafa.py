import string
c=0
for x in input():
    if x in string.ascii_letters:
        c+=1
print(c)