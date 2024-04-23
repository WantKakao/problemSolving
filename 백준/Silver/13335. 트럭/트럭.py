from collections import deque

n, l, w = map(int, input().split())
truck = [*map(int, input().split())]

q = deque([0 for _ in range(l)])
t, i, current_w = 0, 0, 0
while i < n:
    cross = q.pop()
    current_w -= cross

    if truck[i] <= w - current_w:
        q.appendleft(truck[i])
        current_w += truck[i]
        i += 1
    else:
        q.appendleft(0)
    t += 1

print(t+l)