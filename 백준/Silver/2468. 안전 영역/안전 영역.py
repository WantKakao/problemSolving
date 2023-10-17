import sys
sys.setrecursionlimit(10000)    # 재귀 깊이 설정 (기본=1000)
input = sys.stdin.readline

n = int(input())
graph = []
maxs = []

for _ in range(n):
    i = list(map(int, input().split()))
    graph.append(i)
    maxs.append(max(i))


def safe_space(rain, i, j):
    if graph[i][j] > rain and counted[i][j] == False:
        counted[i][j] = True
        if i < n-1 and counted[i+1][j] == False:
            safe_space(rain, i+1, j)
        if i > 0 and counted[i-1][j] == False:
            safe_space(rain, i-1, j)
        if j < n-1 and counted[i][j+1] == False:
            safe_space(rain, i, j+1)
        if  j > 0 and counted[i][j-1] == False:
            safe_space(rain, i, j-1)
        return True
    return False


if max(maxs) > 1:
    counts = []
    for r in range(1, max(maxs)):
        count = 0
        counted = [[False for _ in range(n)] for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if safe_space(r, x, y) == True:
                    count += 1
        counts.append(count)

    print(max(counts))
else:
    print(1)