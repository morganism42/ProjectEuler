import sympy
import itertools

bigprime = 0
for i in range(2, 10):
    nums = range(1, i)
    nums = ''.join(str(k)for k in nums)
    primes = itertools.permutations(nums, len(nums))
    for z in primes:
        num = int(''.join(k for k in z))
        if sympy.isprime(num) and num > bigprime:
            bigprime = num
print(bigprime)
