def sosu(x):
    for j in range(2, int(x**0.5)+1):
        if x%j == 0:
            return False
    return True
s = [x for x in range(2, 10000) if sosu(x)]
n = int(input())
for _ in range(n):
    k = int(input())
    t1 = k//2
    t2 = k - t1
    while True:
        if t1 in s:
            if t2 in s:
                print(t1, t2)
                break
        t1 -= 1
        t2 += 1