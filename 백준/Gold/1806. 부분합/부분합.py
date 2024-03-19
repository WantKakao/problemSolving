n, s = map(int, input().split())
nums = [*map(int, input().split())]
if s == 0:
    print(1)
else:
    nums_sum = 0
    ans = 100001
    left_idx = 0
    for i in range(n):
        nums_sum += nums[i]
        while nums_sum >= s:
            temp = i - left_idx + 1
            if temp < ans:
                ans = temp
            nums_sum -= nums[left_idx]
            left_idx += 1
    if ans == 100001:
        print(0)
    else:
        print(ans)
    