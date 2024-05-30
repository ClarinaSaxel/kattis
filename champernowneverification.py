s,i=input(),1
while len(s)>0:
    if not s.startswith(str(i)):
        i=0;break
    s=s[len(str(i)):]
    i+=1
print(i-1)