import math
sum = 0
for i in range(3,1000000):
    print(i)
    msum = 0
    x = str(i)
    for j in x:
        msum += math.factorial(int(j))
    if msum == i:
        sum += i
print(sum)
