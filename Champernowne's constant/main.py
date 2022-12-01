numbers = '0'
num = 1
while len(numbers) <= 1000000:
    numbers += str(num)
    num += 1
print(int(numbers[1])*int(numbers[10])*int(numbers[100])*int(numbers[1000])*int(numbers[10000])*int(numbers[100000])*int(numbers[1000000]))