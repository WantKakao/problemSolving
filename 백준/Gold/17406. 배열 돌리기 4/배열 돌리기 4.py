import copy
from itertools import permutations
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append([*map(int, input().split())])

rotate = []
for _ in range(K):
    rotate.append([*map(int, input().split())])


def rotate_matrix(g, a, b, s):
    temp_matrix = [[0 for _ in range(2*s+1)] for _ in range(2*s+1)]
    temp_matrix[s][s] = g[a-1][b-1]
    for k in range(1, s+1):
        for j in range(s-k+1, s+k+1):
            temp_matrix[s-k][j] = g[a-k-1][b-s+j-2]
        for j in range(s+k-1, s-k-1, -1):
            temp_matrix[s+k][j] = g[a+k-1][b-s+j]
        for i in range(s-k+1, s+k+1):
            temp_matrix[i][s+k] = g[a-s+i-2][b+k-1]
        for i in range(s+k-1, s-k-1, -1):
            temp_matrix[i][s-k] = g[a-s+i][b-k-1]

    for i in range(2*s+1):
        for j in range(2*s+1):
            g[a-s-1+i][b-s-1+j] = temp_matrix[i][j]


P = permutations(rotate, K)
m = 5000
for p in P:
    new_graph = copy.deepcopy(graph)
    for ra, rb, rs in p:
        rotate_matrix(new_graph, ra, rb, rs)
    temp_m = 5000
    for i in range(N):
        temp_m = min(temp_m, sum(new_graph[i]))
    m = min(temp_m, m)

print(m)