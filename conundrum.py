s,r=input(),0
for i in range(len(s)):
    match i%3:
        case 0: 
            if s[i]=='P':continue
            r+=1
        case 1: 
            if s[i]=='E':continue
            r+=1
        case 2: 
            if s[i]=='R':continue
            r+=1
print(r)