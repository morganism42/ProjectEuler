import sympy

primes = sympy.primerange(10, 1000000)
answer = 0


def primetest(j):
    global answer
    for i in range(1, len(j)):
        if not sympy.isprime(int(j[:i])):
            return
        elif not sympy.isprime(int(j[i:])):
            return
    answer += int(j)


for i in primes:
    print(i)
    primetest(str(i))
print(answer)
