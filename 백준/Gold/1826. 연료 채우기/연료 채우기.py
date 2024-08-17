import sys, heapq
input = sys.stdin.readline

n = int(input())
gas_station = []
for _ in range(n):
    dist, fuel = map(int, input().split())
    gas_station.append((dist, fuel))

dist, fuel = map(int, input().split())
gas_station.sort()

q = []
idx = 0
while idx < n:
    if gas_station[idx][0] <= fuel:
        heapq.heappush(q, -gas_station[idx][1])
    else:
        break
    idx += 1

ans = 0
can_arrive = False
while q:
    if fuel >= dist:
        can_arrive = True
        break
    fuel -= heapq.heappop(q)
    ans += 1
    while idx < n:
        if gas_station[idx][0] <= fuel:
            heapq.heappush(q, -gas_station[idx][1])
        else:
            break
        idx += 1

if can_arrive:
    print(ans)
else:
    print(-1)
