import sys
input = sys.stdin.readline
t = int(input())

for idx in range(t):
    height = list(map(int, input().split()))
    line_up = []
    ans = 0
    for h in height[1:]:
        for l in line_up:
            if h < l:
                ans += 1
        line_up.append(h)

    print(idx+1, ans)