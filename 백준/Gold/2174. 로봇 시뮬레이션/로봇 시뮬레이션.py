a, b = map(int, input().split())
n, m = map(int, input().split())
robots = []
direction = ['N', 'W', 'S', 'E']
move = [(1, 0), (0, -1), (-1, 0), (0, 1)]
for _ in range(n):
    x, y, d = map(str, input().split())
    x, y = int(x), int(y)
    for i in range(4):
        if d == direction[i]:
            d = i
    robots.append([y, x, d])
flag = False
for _ in range(m):
    idx, cmd, rpt = map(str, input().split())
    idx, rpt = int(idx)-1, int(rpt)
    if cmd == 'F':
        for _ in range(rpt):
            robots[idx][0] += move[robots[idx][2]][0]
            robots[idx][1] += move[robots[idx][2]][1]
            if 0 < robots[idx][0] <= b and 0 < robots[idx][1] <= a:
                test = True
                for i in range(n):
                    if robots[i][0] == robots[idx][0] and robots[i][1] == robots[idx][1] and i != idx:
                        test = False
                        break
                if not test:
                    print(f'Robot {idx+1} crashes into robot {i+1}')
                    flag = True
                    break
            else:
                print(f'Robot {idx+1} crashes into the wall')
                flag = True
                break
    elif cmd == 'L':
        robots[idx][2] = (robots[idx][2] + rpt) % 4
    else:
        robots[idx][2] = (robots[idx][2] - rpt) % 4
    if flag:
        break
if not flag:
    print('OK')