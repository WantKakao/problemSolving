import sys
input = sys.stdin.readline

n = int(input())
colored_paper = []
for _ in range(n):
    colored_paper.append([*map(int, input().split())])
b, w = 0, 0
# print(colored_paper)


def same_color(x, y, n):
    global b, w
    total = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            total += colored_paper[i][j]
    if total == n ** 2:
        b += 1
    elif total == 0:
        w += 1
    else:
        same_color(x, y, n//2)
        same_color(x+(n//2), y, n//2)
        same_color(x, y+(n//2), n//2)
        same_color(x+(n//2), y+(n//2), n//2)
    return


same_color(0, 0, n)
print(w)
print(b)