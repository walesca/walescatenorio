A = []
B = []
Inters=[]

for j in range(0,20):
    num1 = int(input())
    A.append(num1)
for k in range(0,20):
    num2 = int(input())
    B.append(num2)

for m in range(0,20):
    for l in range(0,20):
        if(A[l]==B[m]):
            Inters.append(A[l])
            
if(len(Inters)==0):
    print("VAZIO")
else:
    Inters = list(set(Inters))           
    Inters.sort()
    for i in range(0,len(Inters)):
        print(Inters[i])
