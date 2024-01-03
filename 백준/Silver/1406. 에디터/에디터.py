from collections import deque
import sys
input = sys.stdin.readline

text = deque([*map(str, input().rstrip())])
n = int(input())
temp = deque()

for _ in range(n):
    inst = [*map(str, input().rstrip())]
    if inst[0] == 'L':
        if len(text) != 0:
            t = text.pop()
            temp.appendleft(t)
    elif inst[0] == 'D':
        if len(temp) != 0:
            t = temp.popleft()
            text.append(t)
    elif inst[0] == 'B':
        if len(text) != 0:
            text.pop()
    else:
        text.append(inst[2])

for i in text:
    print(i, end='')
for j in temp:
    print(j, end='')