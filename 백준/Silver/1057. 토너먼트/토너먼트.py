n, a, b = map(int, input().split())
i = 1
idx_a, idx_b = 0, 0
while True:
    if n <= 2**i:
        break
    i += 1

while True:
    if a <= 2**i and b <= 2**i:
        i -= 1
    elif a > 2**i and b > 2**i:
        a -= 2**i
        b -= 2**i
        i -= 1
    else:
        print(i+1)
        break