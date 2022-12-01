import math
pent = []
minpair = 10000000000000000
for i in range(1, 10000):
    pent.append(int(i*(3*i-1)/2))
i = 0
notfound = True
while notfound:
    print(i)
    i += 1
    n = i * ((i*3)-1)/2
    for j in range(1,i):
        m = j *((j*3)-1)/2
        if 0 == ((math.sqrt(1+24*(n-m))+1)/6)%1 and 0 == ((math.sqrt(1+24*(n+m))+1)/6)%1:
            print(n-m)
            notfound = False