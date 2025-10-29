n = int(input())
m = int(input())

nums = [[0 for _ in range(n)] for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
i, j, t, N = 0, 0, 0, n*n
while N > 0:
    nums[i][j] = N
    new_i, new_j = i + d[t][0], j + d[t][1]
    if 0 <= new_i < n and 0 <= new_j < n and nums[new_i][new_j] == 0:
        i, j = new_i, new_j
    else:
        t  = (t+1)%4
        i, j = i + d[t][0], j + d[t][1]
    N -= 1
    
for i in range(n):
    print(*nums[i])
    for j in range(n):
        if nums[i][j] == m:
            a, b = i, j
print(a+1, b+1)