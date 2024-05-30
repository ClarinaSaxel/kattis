x,y,z=1,0,0
for c in input():
    match c:
        case 'A': x,y=y,x
        case 'B': y,z=z,y
        case 'C': x,z=z,x
print(1if x==1else 2if y==1else 3)