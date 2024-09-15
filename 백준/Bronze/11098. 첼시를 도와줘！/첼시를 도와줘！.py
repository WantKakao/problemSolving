t = int(input())
for _ in range(t):
    players = []
    n = int(input())
    for _ in range(n):
        cost, name = map(str, input().split())
        players.append((int(cost), name))
    players.sort()
    print(players[-1][1])
