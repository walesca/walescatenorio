
num = 1   
aux = 0
lista = []


while(True):
    num = int(input())
    if(num==0): break
    while(num > 0):    
        reverso = num %10    
        aux = (aux *10) + reverso   
        num = num//10 # ' // ' serve para pegar a parte inteira da divisao   
        lista.append(reverso)

    lista = str(lista).replace(' ', '')
    lista = str(lista).replace(',', '][')
    print lista
    lista = []
    aux = 0


