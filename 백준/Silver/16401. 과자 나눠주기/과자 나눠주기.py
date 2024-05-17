nephew, num_of_snack = map(int, input().split())
snack = [*map(int, input().split())]

left = 1
right = max(snack)
ans = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for s in snack:
        cnt += s // mid

    if cnt >= nephew:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)