import sympy
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


primes = list(sympy.primerange(0, 1000000))
primes.insert(0, 0)
cumsum = []
biggest = 0
longest = 0
sumum = 0
for i in primes:
    sumum += i
    cumsum.append(sumum)
for i in range(0, len(cumsum)):
    if i % 100 == 0:
        print("\n" * 100, f"{i / len(cumsum) * 100}% biggest={biggest} longest={longest}")
    for j in reversed(range(0, len(cumsum))):
        if j - i < longest:
            break
        if cumsum[j] - cumsum[i] < 1000000 and sympy.isprime(cumsum[j] - cumsum[i]):
            if j - i > longest:
                longest = j - i
                biggest = cumsum[j] - cumsum[i]
                break
print(biggest)
