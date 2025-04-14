from collections import deque

n, m = map(int, input().split())  # n: 헛간 개수, m: 연결 정보 수
farm = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    farm[a].append(b)
    farm[b].append(a)

visited = [0] * (n + 1)
distance = [0] * (n + 1)

q = deque()
q.append(1)
visited[1] = 1

while q:
    curr = q.popleft()
    for next_barn in farm[curr]:
        if not visited[next_barn]:
            visited[next_barn] = 1
            distance[next_barn] = distance[curr] + 1
            q.append(next_barn)

max_dist = max(distance)
barns = [i for i, d in enumerate(distance) if d == max_dist]

print(min(barns), max_dist, len(barns))
