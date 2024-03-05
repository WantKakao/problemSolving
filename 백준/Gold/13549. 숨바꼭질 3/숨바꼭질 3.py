from collections import deque

n, k = map(int, input().split())
time = 0
if n >= k:
    print(n-k)
else:
    dp = [-1 for _ in range(k+2)]
    temp = deque()
    while n <= k+1 and dp[n] == -1:
        dp[n] = 0
        temp.append((n, 0))
        n *= 2
    while temp:
        j, idx = temp.popleft()
        t1, t2 = j-1, j+1
        if t1 >= 0:
            while t1 <= k + 1 and dp[t1] == -1:
                dp[t1] = idx+1
                temp.append((t1, idx+1))
                t1 *= 2
        while t2 <= k + 1 and dp[t2] == -1:
            dp[t2] = idx+1
            temp.append((t2, idx+1))
            t2 *= 2
    print(dp[-2])