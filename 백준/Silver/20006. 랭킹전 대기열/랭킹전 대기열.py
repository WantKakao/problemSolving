import sys
input = sys.stdin.readline

p, m = map(int, input().split())
room = []
for _ in range(p):
    l, name = map(str, input().rstrip().split())
    level = int(l)
    flag = 0

    for r in room:
        if abs(r[0][0] - level) <= 10 and len(r) < m:
            r.append((level, name))
            flag = 1
            break

    if not flag:
        room.append([(level, name)])

for r in room:
    if len(r) == m:
        print('Started!')
    else:
        print('Waiting!')
    r.sort(key=lambda x: x[1])
    for lev, nam in r:
        print(lev, nam)