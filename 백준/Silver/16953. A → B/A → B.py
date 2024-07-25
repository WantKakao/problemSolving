from collections import deque

a, b = map(int, input().split())
q = deque()
q.append((a, 1))
is_found = False

while q:
    num, cost = q.popleft()
    num1 = num*2
    num2 = int(str(num)+'1')
    if num1 == b or num2 == b:
        is_found = True
        print(cost+1)
        break
    if num1 < b:
        q.append((num1, cost+1))
    if num2 < b:
        q.append((num2, cost+1))

if not is_found:
    print(-1)