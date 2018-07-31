n = input()

resposta=0
inicio=5
passo=3

i=1

while(i*i<=n/2):
   if((n - inicio) % passo == 0):
      resposta+=1
   inicio += 3;
   passo += 2;
   i+=1

print(resposta)

