from math import factorial

count = 0


def combo(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


for i in range(0, 101):
    if factorial(i) > 1000000:
        for j in range(0, i):
            if combo(i, j) > 1000000:
                count += 1
print(count)
