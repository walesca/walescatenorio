id = ["M", "D", "C", "L", "X", "V", "I"]
valor = [1000,500,100,50,10,5,1]

v = raw_input()
num = 0
ant = 1000

for i in v:
   for j in range(7):
      if i == id[j]:
         if ant < valor[j]:
            num += valor[j]-ant*2
         else:
            num += valor[j]

         ant = valor[j]
         break

if num%5:
	print ("O resto pela divisao por 5 do numero dado e igual a %d!" %(num%5))
else:
	print ("O numero e multiplo de 5!")
