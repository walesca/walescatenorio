
num=1
soma=0
while(num!=0):
   num = int(input())
   aux=num
   if num > 1 & num < 1000000000:
      for i in range(2,num):#((num/2)+1)
          while ((aux % i) == 0):
              aux=aux/i
              soma = soma+i
      if(soma!=0):
          print(soma)
          soma=0
      else: 
          print(num)
   elif num==1: 
      print(num)

