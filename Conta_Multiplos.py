mult = 0
n = int(input())
m = int(input())

for i in range(1,50):
   if(i%n==0 and i%m==0):
      mult+=1

print mult

