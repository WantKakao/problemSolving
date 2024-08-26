from itertools import product

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

p = product(nums, repeat=m)
for c in p:
    for k in c:
        print(k, end=' ')
    print()