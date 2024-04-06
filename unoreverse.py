[k,n]=[int(i)for i in input().split()]
print("NO"if n%2==0and n<2*(k-1)else"YES"if n==1or k==2else"MAYBE")