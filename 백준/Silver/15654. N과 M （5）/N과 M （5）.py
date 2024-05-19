from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
arr = permutations(nums, m)
for p in arr:
    for num in p:
        print(num, end=' ')
    print()