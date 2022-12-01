import sympy


def spiral(N):
    count = 0
    diags = [1]
    for i in range(3, N + 1, 2):
        diags.append(diags[-1] + i - 1)
        diags.append(diags[-1] + i - 1)
        diags.append(diags[-1] + i - 1)
        diags.append(diags[-1] + i - 1)
    for i in diags:
        if sympy.isprime(i):
            count += 1

    return count, count / ((N * 2) - 1)


check = True
n = 7
while check:
    c, p = spiral(n)
    if p > 0.1:
        print(c, p)
        n = int(((10 * c + 1) / 2) + 0.5)  # solved the formula for the ratio of primes to diagonals for 10% since the amount of primes wont go down
    else:
        check = False
        print(n)
# print(spiral(26241))
