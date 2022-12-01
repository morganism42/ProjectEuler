import sympy
from math import sqrt
done = False
n = 1
while not done:

    n+=1
    if not sympy.isprime(n) and n%2 != 0:
        done = True
        for i in sympy.primerange(1,n):
            if sqrt((n-i)/2)%1 ==0:
                done = False

print(n)