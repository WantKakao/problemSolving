table, distance = map(int, input().split())
seatingChart = [*map(str, input())]
isEat = [False for _ in range(table)]
ans = 0

for i in range(table):
    if seatingChart[i] == 'P':
        for d in range(max(0, i-distance), min(table, i+distance+1)):
            if not isEat[d] and seatingChart[d] == 'H':
                isEat[d] = True
                ans += 1
                break

print(ans)