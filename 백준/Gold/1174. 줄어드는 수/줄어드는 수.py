from collections import deque

n = int(input())

nums = []
q = deque(range(10))  # 0,1,2,...,9

while q:
    x = q.popleft()
    nums.append(x)
    last = x % 10
    # 다음에 올 자릿수는 last보다 작은 숫자들(중복 불가)
    for d in range(0, last):
        q.append(x * 10 + d)

nums.sort()

if n > len(nums):
    print(-1)
else:
    print(nums[n-1])
