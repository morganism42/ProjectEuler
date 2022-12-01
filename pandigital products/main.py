import itertools
import math

combos = itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9])
answers = []
num1 = 0
num2 = 0
num3 = 0
x = 0
progress = math.factorial(9)
for i in combos:
    print((x*100 / progress), len(answers))

    for j in range(0, 4):
        for k in range(j, 5 - j):
            num2 = 0
            num1 = 0
            for n in range(0, j + 1):
                num1 *= 10
                num1 += i[n]
            for n in range(j, 6 - j):
                num2 *= 10
                num2 += i[n]
            for n in range(5 - j, 9):
                num3 *= 10
                num3 += i[n]
            if num1 * num2 == num3 and num3 not in answers:
                answers.append(num3)

print(answers)
