s1,s2 = map(str,raw_input().split())

vogal = ["A" , "E" , "I" , "O" , "U", "a" , "e" , "i" , "o" , "u"]
id = [""]*len(s1)
ponto=["!!"]
i=0
aux=1

while(len(s1)>i):
   if((s1[i].isupper() or s2[i].isupper()) or (len(s1)!=len(s2))): 
      print("ERRO") 
      aux=0
      break
   elif((s1[i] == s2[i]) and (s1[i] not in vogal)):
      id[i]="0"
   elif(i%2==0):
      id[i]=s1[i].upper()
   else:
      id[i]=ponto[0]
   i+=1

if aux==1:
   print(''.join(id))

