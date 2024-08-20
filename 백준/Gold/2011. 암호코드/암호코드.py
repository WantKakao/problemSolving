code = input()
n = len(code)

if n == 1:
    if code != '0':
        print(1)
    else:
        print(0)

elif n == 2:
    if (code[0] == '1' and code[1] != '0') or (code[0] == '2' and 0 < int(code[1]) < 7):
        print(2)
    elif (code[0] == '0') or (2 < int(code[0]) and code[1] == '0'):
        print(0)
    else:
        print(1)

else:
    flag = False if code[0] != '0' else True
    for i in range(1, n):
        if (code[i] == code[i-1] == '0') or (code[i] == '0' and 2 < int(code[i-1])):
            flag = True
            break
    if flag:
        print(0)

    else:
        dp = [0 for _ in range(n)]
        dp[0] = 1
        if (code[1] == '1' and code[2] != '0') or (code[1] == '2' and 0 < int(code[2]) < 7):
            if (code[0] == '1' and code[1] != '0') or (code[0] == '2' and 0 < int(code[1]) < 7):
                dp[2] = 3
                dp[1] = 2
            else:
                dp[2] = 2
                dp[1] = 1
        else:
            if code[2] == '0':
                dp[2] = 1
                dp[1] = 1
            else:
                if (code[0] == '1' and code[1] != '0') or (code[0] == '2' and 0 < int(code[1]) < 7):
                    dp[2] = 2
                    dp[1] = 2
                else:
                    dp[2] = 1
                    dp[1] = 1

        for i in range(3, n):
            if (code[i-1] == '1' and code[i] != '0') or (code[i-1] == '2' and 0 < int(code[i]) < 7):
                if (code[i-2] == '1' and code[i-1] != '0') or (code[i-2] == '2' and 0 < int(code[i-1]) < 7):
                    dp[i] = (2 * dp[i-2] + dp[i-3]) % 1000000
                else:
                    dp[i] = (2 * dp[i-2]) % 1000000
            else:
                if code[i] == '0':
                    dp[i] = dp[i-2]
                else:
                    dp[i] = dp[i-1]

        print(dp[n-1])