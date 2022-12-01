from math import sqrt
found = False
n = 143
next = 0
while not found:
    n += 1
    hex = n*(2*n-1)
    if ((sqrt(24*hex+1)+1)/6)%1==0 and (sqrt(8*hex+1)-1)/2%1 ==0:
        next = hex
        found = True



print(next)