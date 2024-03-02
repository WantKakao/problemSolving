N, D = map(int, input().split())
shortCut = []
for _ in range(N):
    s, e, d = map(int, input().split())
    shortCut.append((s, e, d))

dp = [i for i in range(D+1)]
shortCut.sort()
for s in shortCut:
    start, end, distance = s
    if end <= D:
        dp[end] = min(dp[end], dp[start] + distance)
        for i in range(D+1):
            dp[i] = min(dp[i], dp[i-1] + 1)

print(dp[-1])