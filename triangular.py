
num = int(input())
i = 1
tri = -1
while tri < num:
   tri = i*(i+1)*(i+2)
   i = i + 1
if tri == num:
   print(str(i-1) + ' * ' + str(i) + ' * ' + str(i+1) + ' = ' + str(tri))
   print("Verdadeiro")
else: 
   print("Falso")

