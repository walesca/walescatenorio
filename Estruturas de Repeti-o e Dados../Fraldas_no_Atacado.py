#-*- coding: utf-8 -*-

soma=0
while(True):
   num=int(input())
   escolha=raw_input()
   if(num<=2):
      soma+=270 # 270=9*30
   else:
      soma+=180  # 180 =6*30
   if escolha.lower()=="não":
      break

aux = int(soma/100)
if(soma%100):#se soma%100 tiver resto 0, a condicao é satisfeita
   aux+=1

print aux
print ((aux*100)-soma)
