import sys
input = sys.stdin.readline
from collections import deque

v = int(input())
e = int(input())
information = [[] for _ in range(v+1)]
degree = [0 for _ in range(v+1)]
for _ in range(e):
    j, i, c = map(int, input().split())
    information[j].append((c, i))
    degree[j] += 1
# print(information) = [[], [], [], [], [], [(2, 1), (2, 2)], [(2, 5), (3, 3), (4, 4)], [(2, 5), (3, 6), (5, 4)]]
q = deque()
basic = []  # 기본 부품 번호
need = [[] for _ in range(v+1)] # 각 재료가 몇개 필요한지 [(count, part number), ..., (count, part number)]
for i in range(1, v+1):
    if degree[i] == 0:
        basic.append(i)
        need[i].append([1, i])
        q.append((need[i], i))

while q:
    # print(q)
    basics, part = q.popleft()  # basics = 가지고있는[(count, part number), ..., (count, part number)]
    for n in range(1, v+1):
        for c, i in information[n]: # information[n] = 필요한[(count, part number), ..., (count, part number)]
            if i == part:
                degree[n] -= 1
                for count, number in basics:
                    count *= c
                    # need[n].append((count, number)) # 무작정 넣지말고 같은거 모아야 메모리초과 안날듯
                    temp = 0
                    for k in range(len(need[n])):
                        if number == need[n][k][1]:
                            need[n][k][0] += count
                            temp = 1
                            break
                    if temp == 0:
                        need[n].append([count, number])
                if degree[n] == 0:
                    q.append([need[n], n])

need[v].sort(key=lambda x: x[1])
for c, i in need[v]:
    print(i, c)