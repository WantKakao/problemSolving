from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))

arr = permutations(nums, m)
ans_list = []
for p in arr:
    ans_list.append(p)

ans_set = set(ans_list)
ans = list(ans_set)
ans.sort()

for a in ans:
    for num in a:
        print(num, end=' ')
    print()