

def euclides(dividendo, divisor):
    if divisor == 0:
        return dividendo
    else:
        return euclides(divisor, dividendo % divisor)


qtd = int(input())
i=1

while(i<=qtd):
   A,D = map(int, raw_input().split())
   print "MDC("+str(A)+","+str(D)+") =", euclides(A,D)
   i+=1



