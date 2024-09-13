n = int(input())
birth = []
for _ in range(n):
    name, day, month, year = map(str, input().split())
    month = '0'+month if len(month) == 1 else month
    day = '0'+day if len(day) == 1 else day
    b = int(year+month+day)
    birth.append((b, name))
birth.sort()
print(birth[-1][1])
print(birth[0][1])