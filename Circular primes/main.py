import sympy
import itertools
circprim = []
primes = list(sympy.primerange(2, 1000000))
def primecheck(i):
    global circprim
    x = str(i)
    x = [j for j in x]
    for y in range(0,len(x)):
        x = x[1:] + x[:1]
        num = int(''.join(k for k in x))
        if not sympy.isprime(num):
            return
    circprim.append(i)

for i in primes:
    print(i)
    primecheck(i)

print(len(circprim))
