import sys
input = sys.stdin.readline
INF = 1000000

n, R = map(int, input().split())
city = [*map(str, input().split())]
city_idx = {}
for i in range(n):
    city_idx[city[i]] = i
d = int(input())
dest = [*map(str, input().split())]
k = int(input())
price = [[INF for _ in range(n)] for _ in range(n)]
R_price = [[INF for _ in range(n)] for _ in range(n)]
for _ in range(k):
    ride, s, e, c = map(str, input().split())
    cost = int(c)
    start = city_idx[s]
    end = city_idx[e]
    if ride[0] == "M" or ride[0] == "I":
        R_price[start][end] = 0
        R_price[end][start] = 0
    elif ride[1] == "-":
        R_price[start][end] = min(cost / 2, R_price[start][end])
        R_price[end][start] = min(cost / 2, R_price[start][end])
    else:
        R_price[start][end] = min(cost, R_price[start][end])
        R_price[end][start] = min(cost, R_price[start][end])
    price[start][end] = min(cost, price[start][end])
    price[end][start] = min(cost, price[start][end])

for z in range(n):
    for x in range(n):
        for y in range(n):
            price[x][y] = min(price[x][y], price[x][z] + price[z][y])
            R_price[x][y] = min(R_price[x][y], R_price[x][z] + R_price[z][y])

dest_idx = []
for i in range(d):
    dest_idx.append(city_idx[dest[i]])

cost = 0
R_cost = 0
for i in range(d-1):
    cost += price[dest_idx[i]][dest_idx[i+1]]
    R_cost += R_price[dest_idx[i]][dest_idx[i+1]]

if cost > R_cost + R:
    print("Yes")
else:
    print("No")