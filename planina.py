def f(i):
    if i==0:
        return 2
    return 2*f(i-1)-1
print(f(int(input()))**2)