from itertools import permutations

N = int(input())
nums = [i for i in range(1, N+1)]

ans = list(permutations(nums, N))
for a in ans:
    for aa in a:
        print(aa, end=' ')
    print()
