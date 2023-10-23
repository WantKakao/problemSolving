# 무거운 쪽 가리키는 화살표, 가벼운 쪽 가리키는 화살표 두 리스트를 따로 받는다
# visited 를 사용해서 개수를 카운트 한다
# 만약 둘 중 하나의 리스트 원소의 개수가 절반 이상이 된다면 ans 배열에 담는다

import sys
input = sys.stdin.readline

v, e = map(int, input().split())
vertex = [[] for _ in range(v+1)]
reverse_vertex = [[] for _ in range(v+1)]
for _ in range(e):
    i, j = map(int, input().split())
    vertex[i].append(j)
    reverse_vertex[j].append(i)

# print(vertex)
# print(reverse_vertex)


def dfs(x):
    global count
    q = []
    visited = [False for _ in range(v + 1)]
    q.append(x)
    while q:
        y = q.pop()
        for i in vertex[y]:
            if visited[i] == False:
                visited[i] = True
                count += 1
                q.append(i)
    return


def reverse_dfs(x):
    global reverse_count
    q = []
    visited = [False for _ in range(v + 1)]
    q.append(x)
    while q:
        y = q.pop()
        for i in reverse_vertex[y]:
            if visited[i] == False:
                visited[i] = True
                reverse_count += 1
                q.append(i)
    return

ans = set()
# ans.add(1)
# print(ans)
for i in range(1, v+1):
    count, reverse_count = 0, 0
    dfs(i)
    reverse_dfs(i)
    if count >= (v+1)//2 or reverse_count >= (v+1)//2:
        ans.add(i)
print(len(ans))