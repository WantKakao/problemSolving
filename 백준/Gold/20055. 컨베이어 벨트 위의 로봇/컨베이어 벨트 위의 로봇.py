from collections import deque

n, k = map(int, input().split())
belt = deque([*map(int, input().split())])
robot = []
ans = 0

while belt.count(0) < k:
    flag = 0
    b = belt.pop()
    belt.appendleft(b)
    for i in range(len(robot)):
        robot[i] += 1
        if robot[i] == n-1:
            flag = 1
    if flag:
        robot.pop(0)

    flag = 0
    for i in range(len(robot)):
        if belt[robot[i]+1] > 0 and robot[i]+1 not in robot:
            robot[i] += 1
            belt[robot[i]] -= 1
            if robot[i] == n-1:
                flag = 1
    if flag:
        robot.pop(0)

    if belt[0] > 0:
        robot.append(0)
        belt[0] -= 1

    ans += 1

print(ans)