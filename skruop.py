I,v=input,7
for _ in range(int(I())):
    s=I()
    if s=='Skru op!' and v<10:
        v+=1
    if s=='Skru ned!' and v>0:
        v-=1
print(v)