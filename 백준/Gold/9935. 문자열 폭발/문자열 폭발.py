from collections import deque
import sys
input = sys.stdin.readline

text = deque([*map(str, input().rstrip())])
bomb = input().rstrip()
temp = deque()
i = 0

while text:
    t = text.popleft()
    if t == bomb[0]:
        temp.append((t, 1))
        i = 1
    elif t == bomb[i]:
        temp.append((t, i + 1))
        i += 1
    else:
        temp.append((t, 0))
        i = 0

    if i == len(bomb):
        for _ in range(i):
            temp.pop()
        if temp:
            i = temp[-1][1]
        else:
            i = 0

if temp:
    for i in temp:
        print(i[0], end='')
else:
    print("FRULA")
