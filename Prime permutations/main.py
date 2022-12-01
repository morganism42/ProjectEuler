import sympy
import itertools

primes = list(sympy.primerange(1000, 10000))
possibles = []
for i in primes:
    batch2 = []
    batch = list(itertools.permutations(str(i)))
    for sett in batch:
        new = 0
        for x in sett:
            new = new * 10 + int(x)
        batch2.append(new)
    batch3 =[]
    for sett in batch2:
        if not sympy.isprime(sett):
            exit
        batch3.append(sett)
    if len(batch3) >= 3:
        possibles.append(batch3)
maybe = []
for batch in possibles:
    for x in range(0, len(batch) - 2):
        for y in range(x, len(batch) - 1):
            for z in range(y, len(batch)):
                if batch[y] - batch[x] == batch[z] - batch[y]:
                    maybe.append([batch[x], batch[y], batch[z]])
print('maybe')
almost = []
for i in maybe:
    if not(i[0] == i[1] or i[1] == i[2] or i[0] == i[2]):
        almost.append(i)
print(almost)
