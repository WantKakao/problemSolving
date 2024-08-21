N = int(input()) + 1

if N > 1023:
    print(-1)
else:
    ans = [-1 for _ in range(10)]

    dp = [[0 for _ in range(10)] for _ in range(10)]
    for j in range(10):
        dp[0][j] = 1
    for i in range(1, 10):
        for j in range(i, 10):
            dp[i][j] = sum(dp[i-1][:j])

    found = False
    for i in range(10):
        if found:
            break
        for j in range(10):
            N -= dp[i][j]
            if N <= 0:
                N += dp[i][j]
                ans[i] = j
                found = True
                while i > 0:
                    i -= 1
                    for j2 in range(j):
                        N -= dp[i][j2]
                        if N <= 0:
                            N += dp[i][j2]
                            ans[i] = j2
                            j = j2
                            break
                break

    str_ans = [str(a) for a in ans if a != -1]
    print(''.join(reversed(str_ans)))
