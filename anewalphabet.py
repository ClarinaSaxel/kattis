s,r=input().lower(),''
for i in s:
    match i:
        case 'a': r+='@'
        case 'b': r+='8'
        case 'c': r+='('
        case 'd': r+='|)'
        case 'e': r+='3'
        case 'f': r+='#'
        case 'g': r+='6'
        case 'h': r+='[-]'
        case 'i': r+='|'
        case 'j': r+='_|'
        case 'k': r+='|<'
        case 'l': r+='1'
        case 'm': r+='[]\\/[]'
        case 'n': r+='[]\\[]'
        case 'o': r+='0'
        case 'p': r+='|D'
        case 'q': r+='(,)'
        case 'r': r+='|Z'
        case 's': r+='$'
        case 't': r+="']['"
        case 'u': r+='|_|'
        case 'v': r+='\\/'
        case 'w': r+='\\/\\/'
        case 'x': r+='}{'
        case 'y': r+='`/'
        case 'z': r+='2'
        case _: r+=i
print(r)