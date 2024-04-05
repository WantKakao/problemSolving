n = int(input())
arr = [*map(int, input().split())]
M = max(arr)
ans = [[] for _ in range(M+1)]
answer = [0 for _ in range(M+1)]
arr2 = sorted(arr)
for i in arr2:
    if ans[i]:
        for a in ans[i]:
            answer[a] += 1
    for j in range(2*i, M+1, i):
        ans[j].append(i)
for i in arr:
    print(answer[i] - len(ans[i]), end=' ')