c={
    sum([int(x) for x in input().split()]): 1,
    sum([int(x) for x in input().split()]): 2,
    sum([int(x) for x in input().split()]): 3,
    sum([int(x) for x in input().split()]): 4,
    sum([int(x) for x in input().split()]): 5
}
m=max(c.keys())
print(f"{c[m]} {m}")