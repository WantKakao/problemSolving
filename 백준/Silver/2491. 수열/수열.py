n = int(input())
l = list(map(int, input().split()))
dp_up, dp_down = [1 for _ in range(n)], [1 for _ in range(n)]

for i in range(1, n):
    if l[i] >= l[i-1]:
        dp_up[i] = dp_up[i-1] + 1

for i in range(1, n):
    if l[i] <= l[i-1]:
        dp_down[i] = dp_down[i-1] + 1

print(max(max(dp_up), max(dp_down)))