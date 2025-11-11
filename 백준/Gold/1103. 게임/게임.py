import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

dp = [[0] * m for _ in range(n)]      # 각 위치에서 얻을 수 있는 최대 이동 횟수 저장
visited = [[False] * m for _ in range(n)]  # DFS 중 방문 여부 (사이클 탐지용)
ans = 0
cycle = False

def dfs(x, y):
    global cycle
    if cycle:  # 이미 사이클 발견 시 더 진행할 필요 없음
        return 0
    if not (0 <= x < n and 0 <= y < m) or board[x][y] == 'H':
        return 0
    if visited[x][y]:  # 현재 경로 중 재방문 → 사이클
        cycle = True
        return 0
    if dp[x][y]:  # 이미 계산된 결과 재사용
        return dp[x][y]

    visited[x][y] = True
    step = int(board[x][y])
    for dx, dy in [(-step, 0), (step, 0), (0, -step), (0, step)]:
        nx, ny = x + dx, y + dy
        dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    visited[x][y] = False  # 경로 종료 시 해제 (다른 경로 탐색 허용)
    return dp[x][y]

ans = dfs(0, 0)
print(-1 if cycle else ans)
