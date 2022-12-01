sum = 1
for i in range(2, 1001):
    sum += i**i

print(sum%(10**10))
