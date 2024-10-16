s=''
for i in range(5):
    l=input()
    if 'FBI' in l:
        s+=str(i+1)+' '
print('HE GOT AWAY!' if s=='' else s)