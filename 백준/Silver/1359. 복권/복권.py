from itertools import combinations

n, m, k = map(int, input().split())
lottery = [i for i in range(1, n+1)]
C = combinations(lottery, m)
list_C = list(C)
c = len(list_C)
standard = list_C[0]
ans = 0
for comb in list_C:
    if len(set(standard) | set(comb)) <= 2*m-k:
        ans += 1
print(ans/c)