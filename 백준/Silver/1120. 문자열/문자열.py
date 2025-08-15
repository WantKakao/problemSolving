A, B = map(str, input().split())
a, b = len(A), len(B)
ans = 50
for i in range(b-a+1):
    temp = B[i:i+a]
    count = sum(1 for x, y in zip(A, temp) if x == y)
    ans = min(ans, a-count)
print(ans)