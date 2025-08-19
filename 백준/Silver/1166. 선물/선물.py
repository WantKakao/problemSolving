N, L, W, H = map(int, input().split())

left, right = 0.0, float(min(L, W, H))
ans = 0.0

for _ in range(100):  # 반복 횟수 = 정밀도 (100번이면 약 1e-30 수준까지 가능)
    mid = (left + right) / 2
    count = (int(L // mid)) * (int(W // mid)) * (int(H // mid))

    if count >= N:     # 충분히 들어가면 더 크게 시도
        ans = mid
        left = mid
    else:              # 부족하면 줄여야 함
        right = mid

print(ans)
