n = int(input())

k = 1000 - n
ans = 0
while k > 0:
    for i in [500, 100, 50, 10, 5, 1]:
        ans += k // i
        k %= i

print(ans)