I,s=input,0
[n,m]=[int(x) for x in I().split()]
for _ in range(n):
    for l in I():
        match l:
            case '.':s+=20
            case 'O':s+=10
            case '\\':s+=25
            case '/':s+=25
            case 'A':s+=35
            case '^':s+=5
            case 'v':s+=22
print(s)