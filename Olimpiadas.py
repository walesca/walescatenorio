
N, M = map(int, raw_input().split())

v_ouro=[]
v_prata=[]
v_bronze=[]


for i in range(M):
   O,P,B = map(int, raw_input().split())
   v_ouro.append(O)
   v_prata.append(P)
   v_bronze.append(B)


lista=[]

for i in range(N):
   lista.append([0,0,0,0])

for i in v_ouro:
   lista[i-1][0]+=1

for i in v_prata:
   lista[i-1][1]+=1

for i in v_bronze:
   lista[i-1][2]+=1

for i in range(len(lista)):
   lista[i][-1]=i+1

lista.sort()
lista.reverse()

for i in (lista):
   print i[-1]

 
