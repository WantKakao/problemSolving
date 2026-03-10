from itertools import combinations

def is_square(points):
    dist = []
    for (x1, y1), (x2, y2) in combinations(l, 2):
        d = (x1-x2)**2 + (y1-y2)**2
        dist.append(d)
    dist.sort()
    return dist[0] > 0 and \
           dist[0] == dist[1] == dist[2] == dist[3] and \
           dist[4] == dist[5] and \
           dist[4] == 2 * dist[0]

t = int(input())
for _ in range(t):
    l = [list(map(int, input().split())) for _ in range(4)]
    print(int(is_square(l)))