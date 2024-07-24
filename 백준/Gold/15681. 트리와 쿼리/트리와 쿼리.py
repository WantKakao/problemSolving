import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(node, parent):
    subtree_size[node] = 1
    for neighbor in tree[node]:
        if neighbor != parent:
            dfs(neighbor, node)
            subtree_size[node] += subtree_size[neighbor]

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N + 1)]
subtree_size = [0] * (N + 1)

# 트리의 간선 정보를 입력받아 인접 리스트를 구성
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 서브트리 크기 계산을 위한 DFS 호출
dfs(R, -1)

# 쿼리 처리
results = []
for _ in range(Q):
    query = int(input())
    results.append(subtree_size[query])

# 결과를 한 번에 출력
print('\n'.join(map(str, results)))
