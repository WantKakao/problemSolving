import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
for _ in range(N):
    m, v = map(int, input().split())
    jewels.append((m, v))

bags = []
for _ in range(K):
    bags.append(int(input()))

jewels.sort()
bags.sort()

q = []
j = 0
ans = 0
for bag in bags:
    while j < N and jewels[j][0] <= bag:
        heapq.heappush(q, -jewels[j][1])
        j += 1
        
    if q:
        ans += -heapq.heappop(q)

print(ans)
