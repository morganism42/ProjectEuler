from math import sqrt

count = 0
for i in range(2, int(sqrt(100))):
    sqr = i ** 2
    for j in range(len(i) - 1, len(str(sqr))):
        temp = str(sqr)
