a = 0
ans = 0
for _ in range(4):
    x, y = map(int, input().split())
    a += y-x
    if a > ans:
        ans = a
print(ans)