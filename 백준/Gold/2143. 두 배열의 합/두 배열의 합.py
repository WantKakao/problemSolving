import bisect
target = int(input())
a = int(input())
A = [*map(int, input().split())]
b = int(input())
B = [*map(int, input().split())]

dp_A = [[0 for _ in range(a)] for _ in range(a)]
dp_B = [[0 for _ in range(b)] for _ in range(b)]

dp_A[0][0] = A[0]
dp_B[0][0] = B[0]

for j in range(1, a):
    dp_A[0][j] = dp_A[0][j-1] + A[j]
for j in range(1, b):
    dp_B[0][j] = dp_B[0][j-1] + B[j]

for i in range(1, a):
    for j in range(i, a):
        dp_A[i][j] = dp_A[i-1][j] - A[i-1]
for i in range(1, b):
    for j in range(i, b):
        dp_B[i][j] = dp_B[i-1][j] - B[i-1]

set_A = []
set_B = []
for i in range(a):
    for j in range(i, a):
        set_A.append(dp_A[i][j])
for i in range(b):
    for j in range(i, b):
        set_B.append(dp_B[i][j])
set_A.sort()
set_B.sort()

ans = 0
for s1 in set_A:
    t = target - s1
    s = bisect.bisect_left(set_B, t)
    e = bisect.bisect_right(set_B, t)
    ans += (e-s)

print(ans)