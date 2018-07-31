v = map(float, raw_input().split())
media=0
par=0
for i in xrange(0, len(v)):
   if(v[i]>=0 and v[i]%2==0):
      media=media+v[i]
      par+=1
if(media==0):
   print("-1")
else:
   print("%0.2f" %(media/par))

