from collections import deque

n, k = map(int, input().split())
time = 0
if n >= k:
    print(n-k)
else:
    dp = [-1 for _ in range(k+2)]
    temp = deque()
    dp[n] = 0
    temp.append((n, 0))
    n *= 2
    while temp:
        j, idx = temp.popleft()
        t1, t2 = j-1, j+1
        if 0 <= t1 <= k+1 and dp[t1] == -1:
            dp[t1] = idx + 1
            temp.append((t1, idx + 1))
        if t2 <= k + 1 and dp[t2] == -1:
            dp[t2] = idx+1
            temp.append((t2, idx+1))
        if 0 < 2*j <= k+1 and dp[2*j] == -1:
            dp[2*j] = idx+1
            temp.append((2*j, idx+1))
    print(dp[-2])
