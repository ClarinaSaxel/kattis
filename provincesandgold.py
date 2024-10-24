g,s,c=[int(x) for x in input().split()]
b=3*g+2*s+c
print('Province or Gold' if b>7 else 'Duchy or Gold' if b>5 else 'Duchy or Silver' if b>4 else 'Estate or Silver' if b>2 else 'Estate or Copper' if b>1 else 'Copper')