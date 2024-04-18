import sys
input = sys.stdin.readline

n = int(input())
skyline = [0]
high = 0
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    if y > high:
        ans += 1
        skyline.append(y)
    else:
        while True:
            p = skyline.pop()
            if p <= y:
                skyline.append(p)
                break
        skyline.append(y)
        if p != y and y != 0:
            ans += 1
    high = y

print(ans)