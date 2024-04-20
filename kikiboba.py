s=input()
b,k=s.count('b'),s.count('k')
print('boba'if b>k else'kiki'if b<k else'boki'if b==k>0 else'none')