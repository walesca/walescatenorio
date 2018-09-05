def fibonnaci(num):
   if num<=1:
      return 1
   else:
      return fibonnaci(num-1)+fibonnaci(num-2)



num=int(input())
if num==0:
   print "O antidoto nao e necessario"
for i in range(num):
   if i==num-1:
      print fibonnaci(i), "mg/L"
   
