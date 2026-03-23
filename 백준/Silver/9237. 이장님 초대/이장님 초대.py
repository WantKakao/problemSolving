n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
ans = 2
for i in range(n):
    ans = max(ans, l[i]+i+2)
print(ans)