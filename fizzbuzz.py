[x,y,n]=[int(x) for x in input().split()]
for i in range(1,n+1):
    a,b=i%x==0,i%y==0
    print('FizzBuzz'if a and b else'Fizz' if a else'Buzz' if b else i)