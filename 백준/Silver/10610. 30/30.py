import sys
input = sys.stdin.readline

n = input().rstrip()
nums = [int(i) for i in n]
nums.sort()
if nums[0] != 0:
    print(-1)
elif sum(nums) % 3 != 0:
    print(-1)
else:
    for j in range(len(n)):
        print(nums[len(n)-1-j], end='')