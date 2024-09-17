m = 0
p = 0
for _ in range(10):
    a, b = map(int, input().split())
    p += (b-a)
    if p > m:
        m = p
print(m)