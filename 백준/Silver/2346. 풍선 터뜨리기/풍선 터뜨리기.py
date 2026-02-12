from collections import deque

n = int(input())
nums = list(map(int, input().split()))

dq = deque((i+1, nums[i]) for i in range(n))

result = []

while dq:
    idx, move = dq.popleft()
    result.append(idx)

    if not dq:
        break

    if move > 0:
        dq.rotate(-(move - 1))
    else:
        dq.rotate(-move)

print(*result)
