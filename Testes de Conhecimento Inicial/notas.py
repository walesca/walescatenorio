from math import ceil

c = [10000, 5000, 2000, 1000, 500, 200]
m = [100, 50, 25, 10, 5, 1]
n = float(input())
n = int(n*100)

print("NOTAS:")

for i in range(6):
	print("%d nota(s) de R$ %.2f" %(n/c[i], c[i]/100.00))
	
	if n >= c[i]:
		n %= c[i]

print("MOEDAS:")

for i in range(6):
	n = int(ceil(n))
	print("%d moeda(s) de R$ %.2f" %(n/m[i], m[i]/100.00))

	if n >= m[i]:
		n %= m[i]
