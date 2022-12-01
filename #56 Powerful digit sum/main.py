biggest = 0
for a in range(100):
    for b in range(100):
        temp = 0
        for i in str(a**b):
            temp += int(i)
        if temp > biggest:
            biggest = temp
print(biggest)