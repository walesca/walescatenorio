j=0
i=0
while(True):
   dicionario={} 
   n, m = map(int, raw_input().split())
   if n==0 and m==0:
      break

   while(j<n):
      original,alterada= raw_input().split(" -> ")
      dicionario[original]=alterada
      j+=1
   j=0

   while(i<m):
      frase=raw_input()
      for w in dicionario.keys():
         frase=frase.replace(w,dicionario[w])
      print frase
      i+=1
   i=0
