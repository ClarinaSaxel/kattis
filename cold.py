input()
count = 0
for temp in [int(x) for x in input().split()]:
    if temp < 0:
        count += 1
print(count)