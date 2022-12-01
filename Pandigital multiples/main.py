biggestpan = 0
for i in range(1000000):
    print(i)
    for j in range(3, 11):
        test = ''
        for x in range(1, j):
            test += str(i*x)
        if len(test) == 9:
            if '1' in test and '2' in test and '3' in test and '4' in test and '5' in test and '6' in test and '7' in test and '8' in test and '9' in test:
                if int(test) > biggestpan:
                    biggestpan = int(test)
print(biggestpan)
