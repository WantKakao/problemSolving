n = int(input())
l = list(map(int, input().split()))

s = sum(l)
sq = sum(x*x for x in l)

ans = (s*s - sq) // 2
print(ans)
