# -*- coding: utf-8 -*-

n=1
while(True):
   n=int(input()) 
   if(n==0): break
   str=raw_input()
   lista = str.split(" ")
   for str in lista:
      print (str[::-1])

