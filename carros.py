
letra = "a"
velocmedia=0
maiorveloc=0
maiorano=0
i=0
while(True):
   letra = raw_input()
   if(letra.lower()=='n'): break
   ano = int(input())
   veloc = float(input())
   if(veloc>maiorveloc):
      maiorveloc=veloc
   if(ano>maiorano):
      maiorano=ano
   velocmedia=velocmedia+veloc
   i=i+1;
if(maiorano>0):
   print('%.2f' % maiorveloc)
   print(maiorano)
   print('%.2f' %(velocmedia/i))
else:
   print("zero")
