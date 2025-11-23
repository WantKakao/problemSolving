import sys
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())
house = []
for _ in range(n):
    a, b = map(int, input().split())
    house.append((a, b))

q = [(x, y, 0) for _ in range(5)]
for i in range(n):
    temp = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]:
        nx, ny = house[i][0] + dx, house[i][1] + dy
        t = []
        for qx, qy, dq in q:
            ndx, ndy = abs(nx-qx), abs(ny-qy)
            t.append(ndx+ndy+dq)
        temp.append((nx, ny, min(t)))
    q = temp
    
q.sort(key=lambda x: x[2])
print(q[0][2])