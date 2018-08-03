p1,p2 = map(str,raw_input().split())


vogais = ["A" , "E" , "I" , "O" , "U", "a" , "e" , "i" , "o" , "u"]
palavra_crip=""
tam_p1 = len(p1)
tam_p2 = len(p2)
i=0
aux=1

while(tam_p1>i):
   if((p1[i].isupper() or p2[i].isupper()) or (tam_p1!=tam_p2)): 
      print("ERRO") 
      aux=0
      break
   elif((p1[i] == p2[i]) and (p1[i] not in vogais)):
      palavra_crip="0"
   elif(i%2==0):
      palavra_crip=palavra_crip+p1[i].upper()
   else:
      palavra_crip=palavra_crip+"!!"
   i+=1

if aux==1:
   print(palavra_crip)

