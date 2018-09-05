#-*- coding: utf-8 -*-
qtd_macacos = 0
soma_tigre = 0
qtd_cobras = 0
qtd_tigres = 0

while True:
   animal = raw_input()
   peso = float(input())
   pais = raw_input()


   if animal.lower() == "macaco":
      qtd_macacos += 1
   elif animal.lower() == "tigre":
      soma_tigre += peso
      qtd_tigres += 1
   elif animal.lower() == "cobra" and pais.lower() == "venezuela":
      qtd_cobras += 1
	
   escolha = raw_input()
   if escolha.lower() == "parar":
      break

if qtd_tigres==0:
   qtd_tigres = 1

print qtd_macacos
print "%.2f" %(soma_tigre/qtd_tigres)
print qtd_cobras
