n, m = map(int, input().split())
block = [*map(int, input().split())]
ans = 0
for i in range(m):
    mini = 0
    for j in range(i+1, m):
        if block[j] >= block[i]:
            ans += (j-i-1) * (block[i]-mini)
            break
        elif block[j] > mini:
            ans += (j-i-1) * (block[j]-mini)
            mini = block[j]
print(ans)