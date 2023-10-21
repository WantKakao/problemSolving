import sys
input = sys.stdin.readline

v = int(input())
node = [0 for _ in range(v+1)]
arr = list(input().rstrip())
edge = [[] for _ in range(v+1)]

for i in range(v):
    node[i+1] = int(arr[i])
for _ in range(v-1):
    i, j = map(int, input().split())
    edge[i].append(j)
    edge[j].append(i)

# print(node)
# print(edge)
# 1번부터 v번 노드까지 전부다 확인
# node 가 0 인 거에서 출발해서 다시 node 가 0 인 것까지 오는데 확인(되돌아오기 불가)


def search(x):
    global ans
    visited[x] = True
    for i in edge[x]:
        if visited[i] == False:
            if node[i] == 1:
                ans += 1
                continue
            search(i)


ans = 0
for i in range(1, v+1):
    if node[i] == 1:
        visited = [False for _ in range(v + 1)]
        search(i)    # 길 확인
print(ans)