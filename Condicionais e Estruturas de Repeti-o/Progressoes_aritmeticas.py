n = int(input())
sequencia = map(int, raw_input().split())

contador = 1

diferenca = sequencia[0] - sequencia[1]

for i in range(1,n-1):
    if(sequencia[i] - sequencia[i+1] != diferenca):
        contador+=1
        if(i+2 < n):
            diferenca = sequencia[i+1] - sequencia[i+2]
        
print(contador)
