
tam_arrays = raw_input()
numerosComoString = tam_arrays.split(" ")
tamanho_arrays = [int(numero) for numero in numerosComoString]
nA,nB = tamanho_arrays

qtd_num = raw_input()
numerosComoString2 = qtd_num.split(" ")
qtd_numeros = [int(numero2) for numero2 in numerosComoString2]
k,m = qtd_numeros

A = []
B = []

array_A = raw_input()
numerosComoString3 = array_A.split(" ")
qtd_num_array_A = [int(numero3) for numero3 in numerosComoString3]
A = qtd_num_array_A

array_B = raw_input()
numerosComoString4 = array_B.split(" ")
qtd_num_array_B = [int(numero4) for numero4 in numerosComoString4]
B = qtd_num_array_B

          
A.sort()         
B.sort()

maior = max(A[:k])
menor = min(B[:m]) 

print(A[:k])
print(B[:m])

if(maior<menor): print("YES")
else: print("NO")
