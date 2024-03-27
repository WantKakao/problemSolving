n = int(input())
m = int(input())
friends = [[10 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a][b] = 1
    friends[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])

ans = 0
for i in range(n+1):
    if friends[1][i] <= 2:
        ans += 1
if friends[1][1] <= 2:
    ans -= 1

print(ans)
