num = 1
cont = True
while (cont):
    if len(str(num)) == len(str(num * 6)):
        if sorted(str(num)) == sorted(str(num * 2)) and sorted(str(num)) == sorted(str(num * 3)) and sorted(
                str(num)) == sorted(str(num * 4)) and sorted(str(num)) == sorted(str(num * 5)) and sorted(
                str(num)) == sorted(str(num * 6)):
            print(f'success {num}')
            break
        else:
            print(f'fail {num}')
    num += 1
