a, b = map(int, input().split())
e = int(b**0.5) + 1

nums = [True for _ in range(b - a + 1)]

for n in range(2, e):
    n2 = n**2
    m, M = a // n2, b // n2
    if a % n2 != 0:
        m += 1
    for k in range(m, M+1):
        nums[n2 * k - a] = False

print(b - a + 1 - nums.count(False))