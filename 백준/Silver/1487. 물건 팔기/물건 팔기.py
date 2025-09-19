n = int(input())
house = []
for _ in range(n):
    p, d = map(int, input().split())
    house.append((p, d))
house.sort()

PROFIT = 0
ans = 0
for i in range(n):
    price = house[i][0]
    profit = 0
    for j in range(n):
        if price <= house[j][0]:
            profit += max(price - house[j][1], 0)
    if profit > PROFIT:
        ans = price
        PROFIT = profit
            
print(ans)