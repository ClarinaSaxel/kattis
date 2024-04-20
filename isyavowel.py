import re
s=input()
v=len(re.findall('[aeiou]',s))
print(v,v+s.count('y'))