n, m = map(int, input().split())
square = []
answer = 1
for _ in range(n):
    square.append(list(int(c) for c in input()))
for i in range(n):
    for j in range(m):
        for s in range(1, min(n-i, m-j)):
            if square[i][j] == square[i+s][j] == square[i][j+s] == square[i+s][j+s]:
                answer = max(answer, (s+1)**2)
print(answer)