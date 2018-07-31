qtd_pessoas=0
peso=0

while True:
    n = float(input())
    if not n: break #se n nao for true(1),ou seja, n igual a 0, break

    if peso+n <= 560 and qtd_pessoas < 7:
        peso += n
        qtd_pessoas += 1
    else: break

print "%d\n%.1f" %(qtd_pessoas, peso)
