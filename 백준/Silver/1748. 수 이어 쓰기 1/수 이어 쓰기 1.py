n = int(input())
l = len(str(n))
a = 0
for i in range(l, 0, -1):
    if i == l:
        t = n - (10**(i-1)) + 1
    else:
        t = (10**i) - (10**(i-1))
    a += (i*t)
print(a)