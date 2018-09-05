

lista=[""]

for w in range(10):
   string=raw_input()
   lista.append(string)

c=raw_input()

for i in range(1,11):
   for j in range(len(lista[i])):
      if lista[i][j]==c.lower() or lista[i][j]==c.upper() :
        print lista[i]


