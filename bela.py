I=input
l,s=[x for x in I().split()],0
n,b=int(l[0]),l[1]
for i in range(n*4):
    r=I()
    match r[0]:
        case 'A':s+=11
        case 'K':s+=4
        case 'Q':s+=3
        case 'T':s+=10
        case 'J':
            if r[1]==b:s+=20
            else:s+=2
        case '9':
            if r[1]==b:s+=14
print(s)