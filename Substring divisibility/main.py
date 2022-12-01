import itertools
nums = '0123456789'
pans = itertools.permutations(nums)
sum = 0
k = 1
for i in pans:
    number = ''.join(k for k in i)
    if int(number[1:4])%2 == 0 and int(number[2:5])%3 == 0 and int(number[3:6])%5 == 0 and int(number[4:7])%7 == 0 and int(number[5:8])%11 == 0 and int(number[6:9])%13 == 0 and int(number[7:10])%17 == 0:
        sum+=int(number)
print(sum)