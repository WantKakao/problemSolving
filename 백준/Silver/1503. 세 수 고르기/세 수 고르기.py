N, M = map(int, input().split())
S = set()
if M > 0:
    S = set(map(int, input().split()))

# 후보 숫자들 (1~2000까지만)
candidates = [i for i in range(1, 1002) if i not in S]

ans = float('inf')

for x in candidates:
    for y in candidates:
        if x * y > 132651:  # 어차피 너무 커짐
            break
        for z in candidates:
            val = x * y * z
            if val > 132651:  # 2000 넘어가면 볼 필요 없음
                break
            diff = abs(N - val)
            if diff < ans:
                ans = diff

print(ans)
