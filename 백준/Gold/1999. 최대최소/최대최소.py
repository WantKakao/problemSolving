from collections import deque
import sys
input = sys.stdin.readline

N, B, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
queries = [list(map(int, input().split())) for _ in range(K)]

# 1️⃣ 행 기준 슬라이딩 윈도우
row_min = [[0]*(N-B+1) for _ in range(N)]
row_max = [[0]*(N-B+1) for _ in range(N)]

for i in range(N):
    min_dq, max_dq = deque(), deque()
    for j in range(N):
        # 최소값 deque
        while min_dq and matrix[i][min_dq[-1]] >= matrix[i][j]:
            min_dq.pop()
        min_dq.append(j)
        if min_dq[0] <= j - B:
            min_dq.popleft()

        # 최대값 deque
        while max_dq and matrix[i][max_dq[-1]] <= matrix[i][j]:
            max_dq.pop()
        max_dq.append(j)
        if max_dq[0] <= j - B:
            max_dq.popleft()

        if j >= B - 1:
            row_min[i][j - B + 1] = matrix[i][min_dq[0]]
            row_max[i][j - B + 1] = matrix[i][max_dq[0]]

# 2️⃣ 열 기준 슬라이딩 윈도우
sub_matrix = [[0]*(N-B+1) for _ in range(N-B+1)]

for j in range(N-B+1):
    min_dq, max_dq = deque(), deque()
    for i in range(N):
        # 세로 최소값
        while min_dq and row_min[min_dq[-1]][j] >= row_min[i][j]:
            min_dq.pop()
        min_dq.append(i)
        if min_dq[0] <= i - B:
            min_dq.popleft()

        # 세로 최대값
        while max_dq and row_max[max_dq[-1]][j] <= row_max[i][j]:
            max_dq.pop()
        max_dq.append(i)
        if max_dq[0] <= i - B:
            max_dq.popleft()

        if i >= B - 1:
            sub_matrix[i - B + 1][j] = row_max[max_dq[0]][j] - row_min[min_dq[0]][j]

# 3️⃣ 질의 처리
for i, j in queries:
    print(sub_matrix[i-1][j-1])
