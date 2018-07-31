

prog2 = []
prog3 = []
Inters=[]

prog2 = map(int, raw_input().split())
prog3 = map(int, raw_input().split())

for m in range(0,45):
    for l in range(0,30):
        if(prog2[m]==prog3[l]):
            Inters.append(prog2[m])

for n in range(0,len(Inters)):
    print Inters[n],

print(" \n")
