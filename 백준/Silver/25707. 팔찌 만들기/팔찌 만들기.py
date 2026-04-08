n = int(input())
l = list(map(int, input().split()))

ans = 0
l.sort()
for i in range(1, n):
    ans += (l[i] - l[i-1])
ans += (l[-1] - l[0])
print(ans)