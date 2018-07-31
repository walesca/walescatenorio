x,y = map(int, raw_input().split())
flag = True

for i in range(x, y+1):
   if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
      print i
      flag = False

if flag:
   print -1
