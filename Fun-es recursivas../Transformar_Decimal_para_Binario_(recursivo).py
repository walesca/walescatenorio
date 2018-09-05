def binario(value):
   if value==0:
      return
   else:
      binario(value/2)
      print value%2

n = input()
if n!=0:
   binario(n)
else:
   print 0
