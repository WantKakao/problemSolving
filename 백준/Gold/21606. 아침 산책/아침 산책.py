import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
v = int(input())
node = [0] + list(map(int, input().rstrip()))
edge = [[] for _ in range(v+1)]
cnt = 0 # 실내끼리 붙어있는 경우 체크
for _ in range(v-1):
    i, j = map(int, input().split())
    edge[i].append(j)
    edge[j].append(i)
    if node[i] == node[j] == 1:
        cnt += 2

# print(node)
# print(edge)


def search(x):  # 실외 기준
    global ans
    visited[x] = True
    for i in edge[x]:
        if visited[i] == False:
            if node[i] == 1:
                ans += 1
                continue
            search(i)


visited = [False for _ in range(v + 1)]
for i in range(1, v+1):
    if not visited[i] and node[i] == 0:
        ans = 0
        search(i)    # 길 확인
        cnt += ans * (ans-1)

print(cnt)