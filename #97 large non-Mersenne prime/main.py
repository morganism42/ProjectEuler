start = 28433
for i in range(0, 7830457):
    print(f'{int(i / 7830457 * 100)}%')
    start *= 2
    if len(str(start)) > 10:
        start = int(str(start)[-10:])
start += 1
print(str(start))
