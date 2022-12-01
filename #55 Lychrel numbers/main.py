def lychrel(number):
    for j in range(49):
        number += int(str(number)[::-1])
        if number == int(str(number)[::-1]):
            return False
    return True


amount = 0
for i in range(10000):
    if lychrel(i):
        amount += 1
print(amount)
