n = input()

v = map(int, raw_input().split())
 #inicia na posicao n-1, de 1 em 1, voltando (-1), ate o fim (-1)
#(inicio, ate o fim, de 1 em 1)
for i in xrange(n-1, -1, -1): #xrange fornece melhor desempenho em alguns casos
   print v[i],#ordem inversa
print

for i in xrange(1, n):
   print v[i], #deslocamento para a esquerda
print v[0]

v.sort() #ordena em ordem crescente
v.reverse() #coloca a lista em ordem inversa

for i in v:
   print i, #ordenado em ordem decrescente


