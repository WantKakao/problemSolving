n = int(input())

level = []
for _ in range(n):
    level.append(int(input()))

ans = 0
for i in range(n-1, 0, -1):
    if level[i] <= level[i-1]:
        ans += level[i-1] - level[i] + 1
        level[i-1] = level[i] - 1

print(ans)