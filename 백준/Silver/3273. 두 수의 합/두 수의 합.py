n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()
i, j = 0, n-1
ans = 0

while i < j:
    if nums[i] + nums[j] == x:
        ans += 1
        i += 1
        j -= 1
    elif nums[i] + nums[j] > x:
        j -= 1
    else:
        i += 1

print(ans)