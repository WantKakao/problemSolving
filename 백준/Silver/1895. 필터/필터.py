import sys
input = sys.stdin.readline

n, m = map(int, input().split())
image = []
for _ in range(n):
    image.append(list(map(int, input().split())))
t = int(input())

ans = 0
for i in range(n-2):
    for j in range(m-2):
        temp = []
        for a in range(i, i+3):
            for b in range(j, j+3):
                temp.append(image[a][b])
        temp.sort()
        if temp[4] >= t:
            ans += 1
print(ans)