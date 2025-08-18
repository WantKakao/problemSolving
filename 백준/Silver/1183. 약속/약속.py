n = int(input())
interval = []
for _ in range(n):
    A, B = map(int, input().split())
    interval.append(A-B)

interval.sort()
i = len(interval)
if i == 1:
    if interval[0] % 2 == 0:
        print(2)
    else:
        print(1)
else:
    if i % 2 == 0:
        print(interval[i // 2] - interval[i // 2 - 1] + 1)
    else:
        print(1)