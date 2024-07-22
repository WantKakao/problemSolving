T = int(input())

for _ in range(T):
    N = int(input())
    S = input()

    target = ''
    for num in S:
        if num == '1':
            target += '0'
        else:
            target += '1'

    ans = 0
    for idx in range(N):
        if ans != 0:
            break

        if S[idx] == '0':
            temp = S[idx:]
            lt = len(temp)
            for idx_s in range(idx+1):
                if S[idx_s] == '1':
                    decimal = int(S[idx_s:idx_s+lt], 2) ^ int(S, 2)
                    ans = max(ans, decimal)

    if '1' in S:
        decimal = int('1', 2) ^ int(S, 2)
        ans = max(ans, decimal)
    if '0' in S:
        decimal = int('0', 2) ^ int(S, 2)
        ans = max(ans, decimal)
    print(bin(ans)[2:])