import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

v = int(input())
edge = [[] for _ in range(v+1)]
parent = [i for i in range(v+1)]
visited = [False for _ in range(v+1)]

for _ in range(v-1):
    i, j = map(int, input().split())
    edge[i].append(j)
    edge[j].append(i)

def p(x):
    # print(parent)
    for i in edge[x]:
        if visited[i] == False:
            visited[i] = True
            parent[i] = x
            p(i)


p(1)
for i in range(2, v+1):
    print(parent[i])