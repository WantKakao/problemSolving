days = int(input())
schedule = []
for _ in range(days):
    need_days, profit = map(int, input().split())
    schedule.append((need_days, profit))

profit = [0] * (days + 1)
for day in range(days):
    profit[day] = max(profit[day], profit[day - 1])
    if day + schedule[day][0] <= days:
        profit[day + schedule[day][0]] = max(profit[day + schedule[day][0]], profit[day] + schedule[day][1])

print(max(profit[-1], profit[-2]))