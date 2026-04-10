from math import comb

while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(comb(a, b))