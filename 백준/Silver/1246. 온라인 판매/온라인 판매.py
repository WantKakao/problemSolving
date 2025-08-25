n, m = map(int, input().split())
A = []
for _ in range(m):
    A.append(int(input()))
A.sort(reverse=True)
k = min(n, m)
A = A[:k]
A.sort()
ans = 0
for i in range(k):
    temp = A[i] * (k-i)
    if temp > ans:
        ans = temp
        cnt = (A[i])
print(cnt, ans)