from collections import deque
import sys
input = sys.stdin.readline

d = deque()
t = int(input())
for _ in range(t):
    s = input()
    if s[0] == '1':
        d.appendleft(int(s[2:]))
    elif s[0] == '2':
        d.append(int(s[2:]))
    elif s[0] == '3':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif s[0] == '4':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif s[0] == '5':
        print(len(d))
    elif s[0] == '6':
        if d:
            print(0)
        else:
            print(1)
    elif s[0] == '7':
        if d:
            print(d[0])
        else:
            print(-1)
    else:
        if d:
            print(d[-1])
        else:
            print(-1)