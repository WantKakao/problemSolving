import sys
input = sys.stdin.readline

n = int(input())
town = []
for _ in range(n):
    l, p = map(int, input().split())
    town.append((l, p))
town.sort()

total_p = sum(a for _, a in town)
cumulative_p = 0
for loc, pop in town:
    cumulative_p += pop
    if cumulative_p >= (total_p + 1) // 2:
        print(loc)
        break