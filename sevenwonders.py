s=input()
c,g,t=s.count('C'),s.count('G'),s.count('T')
r=c**2+g**2+t**2
if c>0and g>0and t>0:r+=7*min(c,g,t)
print(r)