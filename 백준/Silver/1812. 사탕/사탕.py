import sys
input = sys.stdin.readline

nums = []
n = int(input())
for _ in range(n):
    nums.append(int(input()))

s = 0
for i in range(n):
    if i % 2 == 0:
        s += nums[i]
    else:
        s -= nums[i]

t = s // 2

for i in range(n-1):
    print(t)
    t = nums[i] - t
print(t)