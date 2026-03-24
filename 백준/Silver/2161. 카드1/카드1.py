from collections import deque
n = int(input())
q = deque()
for i in range(1, n+1):
    q.append(i)
print(q.popleft(), end=' ')
while q:
    x = q.popleft()
    q.append(x)
    print(q.popleft(), end=' ')