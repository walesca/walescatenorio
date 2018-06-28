#include <stdio.h>
#include <math.h>

int primes[50000] = {2};

bool isPrime(int x) {
	for(int i=2; i*i <= x; ++i)
		if(x%i == 0) return false;

	return true;
}

int main()
{
	int x, root;
	int size = 0;
	int answer;

	for(int i=3; i<=100000; i+=2) {
		if(isPrime(i))
			primes[++size] = i;
	}

	while(scanf("%d", &x) && x)
	{
		answer = 0;
		root = sqrt(x);

		if(isPrime(x)) {
			printf("%d\n", x);
		} else if(x == root*root && isPrime(root)) {
			printf("%d\n", root+root);
		} else {
			int k = 0;

			while(x != 1)
			{
				while(x % primes[k] == 0) {
					//printf("fatorando por: %d\n", primes[k]);
					x /= primes[k];
					answer += primes[k];
				}

				if(x!=1 && isPrime(x)) {
					answer += x;
					break;
				}

				++k;
			}

			printf("%d\n", answer);
		}
	}
	return 0;
}

