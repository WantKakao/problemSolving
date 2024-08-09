from collections import deque
n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])
i = 1
ans = []
while q:
    t = q.popleft()
    if i != k:
        q.append(t)
        i += 1
    else:
        ans.append(str(t))
        i = 1

print('<', end='')
print(', '.join(ans), end='')
print('>', end='')