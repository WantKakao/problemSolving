import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    start = [*map(int, input().split())]
    conv = []
    for _ in range(n):
        conv.append([*map(int, input().split())])
    end = [*map(int, input().split())]
    visited = [0 for _ in range(n)]

    q = deque()
    q.append((start[0], start[1]))
    flag = 1
    while q:
        x, y = q.popleft()
        if abs(end[1]-y) + abs(end[0]-x) <= 1000:
            print('happy')
            flag = 0
            break
        for i in range(n):
            if abs(conv[i][1]-y) + abs(conv[i][0]-x) <= 1000 and not visited[i]:
                q.append((conv[i][0], conv[i][1]))
                visited[i] = 1
    if flag:
        print('sad')
