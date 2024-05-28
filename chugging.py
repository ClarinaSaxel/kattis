I,r,s=input,0,0
f,[t,d],[u,e]=int(I()),[int(x) for x in I().split()],[int(y) for y in I().split()]
for i in range(f):r,s=r+t+i*d,s+u+i*e
print('Bob'if r>s else'Alice'if r<s else'=')