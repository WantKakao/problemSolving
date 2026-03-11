from itertools import permutations

n = int(input())
L = list(map(int, input().split()))
answer = 0
for l in permutations(L, n):
    ans = 0
    for i in range(1, n):
        ans += abs(l[i] - l[i-1])
    answer = max(answer, ans)
print(answer)