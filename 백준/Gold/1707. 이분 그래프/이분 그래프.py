import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

k = int(input())


def cycle(i, v):
    ''' -1 과 1 을 번갈아 적용 '''
    visited[i] = v
    for e in edge[i]:
        if visited[e] == 0: # 아직 미방문시
            result = cycle(e, -v)
            if not result:
                return False
        if visited[e] == v:
            return False
    return True


for _ in range(k):
    v, e = map(int, input().split())
    edge = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    for _ in range(e):
        i, j = map(int, input().split())
        edge[i].append(j)
        edge[j].append(i)

    for i in range(1, v+1):
        if visited[i] == 0:
            result = cycle(i, 1)
            if not result:
                break
    print('YES') if result else print('NO')