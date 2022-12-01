import math
maxsolutions = 0
mostsolutions = 0
for k in range(1, 1001):
    print(k)
    solutions = 0
    for i in range(1, k):
        for j in range(1, k-i):
            if math.sqrt(i**2+j**2)%1 == 0 and math.sqrt(i**2+j**2)+i+j == k:
                solutions += 1
    if solutions > mostsolutions:
        maxsolutions = k
        mostsolutions = solutions
print(maxsolutions)