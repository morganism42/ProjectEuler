import sympy

primes = list(sympy.primerange(1000, 10000))
nextprimes = []
for x in range(0, len(primes)):
    for y in range(x + 1, len(primes)):
        if sympy.isprime(primes[y] + (primes[y] - primes[x])):
            if(sorted(str(primes[x])) == sorted(str(primes[y])) == sorted(str(primes[y] + (primes[y] - primes[x])))):
                print(primes[x],primes[y],primes[y] + (primes[y] - primes[x]))