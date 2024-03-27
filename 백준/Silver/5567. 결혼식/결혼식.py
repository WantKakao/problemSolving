import copy

n = int(input())
m = int(input())
friends = [[10 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a][b] = 1
    friends[b][a] = 1

ans = 0
temp = []
for j in range(1, n+1):
    if friends[1][j] == 1:
        temp.append(j)
        ans += 1
l = copy.deepcopy(temp)
for i in l:
    for j in range(1, n+1):
        if friends[i][j] == 1 and j not in temp:
            ans += 1
            temp.append(j)

if 1 in temp:
    ans -= 1
print(ans)
