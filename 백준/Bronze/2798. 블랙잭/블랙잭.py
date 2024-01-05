from itertools import combinations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
comb = list(combinations(arr, 3))
for i in comb:
    ans.append(sum(i))
ans.sort()
k = 0
for j in ans:
    if j > m:
        break
    if j > k:
        k = j
print(k)