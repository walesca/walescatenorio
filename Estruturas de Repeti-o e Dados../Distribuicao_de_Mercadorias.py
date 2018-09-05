
i=0
caminhao_0=0
caminhao_1=0
n_dias_0=0
n_dias_1=0
maior=[]
preco=0

N=int(input())
while(i<N):
   peso=int(input())
   entrega=int(input())
   distancia=int(input())
   if entrega==0:
      if peso>=10:
         if peso%10!=0:
            caminhao_0+=((peso/10)+1)
         else:
            caminhao_0+=(peso/10)
      if distancia>=100:
         if distancia%100!=0:
            n_dias_0+=((distancia/100)+1)
            maior.append(n_dias_0)
         else:
            n_dias_0+=(distancia/100)
            maior.append(n_dias_0)
   else:
       if peso>=5:
          if peso%5!=0:
            caminhao_1+=((peso/5)+1)
          else:
            caminhao_1+=(peso/5)
       if distancia>=250:
          if distancia%250!=0:
            n_dias_1+=((distancia/250)+1)
            maior.append(n_dias_1)
          else:
            n_dias_1+=(distancia/250)
            maior.append(n_dias_1)
       
   i+=1

maior.sort()
maior.reverse()

preco=(caminhao_0*500)+(caminhao_1*1200)
caminhao=caminhao_0+caminhao_1
print caminhao,preco,maior[0]


