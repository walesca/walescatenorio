n = int(input())
vetor_danos = []

for i in range(n):
   x,y = map(int,raw_input().split())
   vetor_danos.append((y,x))

vetor_danos.sort()
vetor_danos.reverse()

y = int(input())
hp = 100

for dano in vetor_danos:
   hp -= dano[-1]

   if hp <= 0:
      print 'Inimigo Morto'
      break

   hp += dano[0]
else:
   print 'Inimigo Vivo'

