
contador=2
numero,numero2=map(int,raw_input().split())
j=0
maior=-1
primos=[]
frequencia=[0]*50
for i in range(numero,numero2+1):
   limite=int(i ** 0.5)
   contador=2
   while(contador<=limite):
       if i%contador==0:
           break
       contador=contador+1

   if contador==limite+1:
       primos.append(i)

for i in range(1,len(primos)):
   frequencia[primos[i]-primos[i-1]]+=1
   aux=frequencia[primos[i]-primos[i-1]]
   if aux>frequencia[maior]:
      maior=primos[i]-primos[i-1]
   elif aux==frequencia[maior]:
      maior=-1

print maior



