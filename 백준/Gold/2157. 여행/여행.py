import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
flight = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(k):
    a, b, c = map(int, input().split())
    if a < b:  # 서쪽으로만 이동
        flight[a][b] = max(flight[a][b], c)

# dp[i][j] = i번 도시에 j개 도시를 거쳐 도달할 때의 최대 점수
dp = [[-1] * (m+1) for _ in range(n+1)]
dp[1][1] = 0  # 1번 도시에서 시작 (도시 1개 방문, 점수 0)

for i in range(1, n+1):
    for cnt in range(1, m):  # 도시 cnt개를 거쳐 i번에 도달
        if dp[i][cnt] == -1:
            continue
        
        for j in range(i+1, n+1):
            if flight[i][j] > 0:
                new_score = dp[i][cnt] + flight[i][j]
                dp[j][cnt+1] = max(dp[j][cnt+1], new_score)

# N번 도시에 도달한 모든 경우 중 최댓값
answer = max(dp[n][1:m+1])
print(answer if answer != -1 else 0)