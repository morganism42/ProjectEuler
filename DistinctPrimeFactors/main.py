from math import sqrt
import sympy

done = False
n = 4
flist = [1, 1, 1, 1]
while not done:
    print(n)
    n += 1
    if sympy.isprime(n):
        flist.append(1)
    else:
        flist.append(0)
        for i in sympy.primerange(1, n/2):
            if n % i == 0:
                flist[-1] += 1
    if flist[-1] == 4 and flist[-2] == 4 and flist[-3] ==4 and flist[-4] == 4:
        done = True
        print(n-3)
