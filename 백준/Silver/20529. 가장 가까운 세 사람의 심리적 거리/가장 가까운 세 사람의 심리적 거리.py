from itertools import combinations
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(input().split())

    all_MBTI = []
    for MBTI in arr:
        if all_MBTI.count(MBTI) < 3:
            all_MBTI.append(MBTI)

    temp = combinations(all_MBTI, 3)
    ans = 12
    for mbti1, mbti2, mbti3 in temp:
        cnt = 0
        for i in range(4):
            if mbti1[i] != mbti2[i]:
                cnt += 1
            if mbti2[i] != mbti3[i]:
                cnt += 1
            if mbti3[i] != mbti1[i]:
                cnt += 1
        if cnt < ans:
            ans = cnt

    print(ans)