sum = 0
for i in range(0,1000000):
    #print(f'{i/10000}%')
    num = i
    numr = int(str(i)[::-1])
    if num == numr:
        numb = str(bin(num))
        numb = numb[2:]
        numbr = numb[::-1]
        print(numb,numbr)
        if numb == numbr:
            sum += i
print(sum)