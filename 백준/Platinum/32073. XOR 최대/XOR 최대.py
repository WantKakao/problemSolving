T = int(input())

for _ in range(T):
    N = int(input())
    S = input()

    idx = -1
    r_idx = -1
    for i in range(1, N):
        if S[i-1] == '1' and S[i] == '0':
            idx = i
            break
        if S[i-1] == '0' and S[i] == '1':
            r_idx = i

    # 전부 1 이거나 전부 0 일때
    if idx == r_idx == -1:
        if S[0] == '0':
            print(0)
        else:
            print('1'*(N-1)+'0')

    # 0 에서 1 로 바뀌는 것만 있을때
    elif idx == -1:
        ans = 0 ^ int(S, 2)
        print(bin(ans)[2:])

    else:
        ans_idx = idx-1
        comp = S[idx:]
        l = len(comp)
        for i in range(1, l):
            if comp[i] == '1':
                break
            else:
                if ans_idx-1 >= 0 and S[ans_idx-1] == '1':
                    ans_idx -= 1
                else:
                    break

        k = int(S[ans_idx:ans_idx+l], 2) ^ int(S, 2)
        print(bin(k)[2:])
