
def solve(i, f, c, k, d):
   if(i == f):
      return abs(c-k) == d

   op1 = solve(i+1, f, c+1, k, d) #cara
   op2 = solve(i+1, f, c, k+1, d) #coroa
   return op1 + op2

n,d = map(int,raw_input().split())
print solve(0, n, 0, 0, d)

