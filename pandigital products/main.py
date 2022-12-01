import itertools

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

perms = itertools.permutations(digits)
final = []
for sequence in perms:

    for x in range(1, 8):
        num1 = 0
        for i in range(0, x):
            num1 = num1 * 10 + sequence[i]
        for y in range(x, 9):
            num2 = 0
            num3 = 0
            for i in range(x, y):
                num2 = num2 * 10 + sequence[i]
            for i in range(y, 9):
                num3 = num3 * 10 + sequence[i]
            if num1 * num2 == num3:
                if num3 not in final:
                    final.append(num3)
print(sum(final))