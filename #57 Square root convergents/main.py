from decimal import Decimal
from fractions import Fraction

n = d = 1

results = 0
for i in range(1000):
    np = n
    dp = d
    n = n + 2 * d
    d = np + d
    if len(str(n)) > len(str(d)):
        results += 1
print(results)
