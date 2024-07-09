from itertools import combinations

n, m = map(int, input().split())
arr = [*map(int, input().split())]
arr.sort()

comb = combinations(arr, m)
for c in comb:
    for num in c:
        print(num, end=' ')
    print()