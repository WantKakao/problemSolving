import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append([*map(int, input().split())])

for i in range(n):
    for j in range(m):
        if i == 0:
            if j != 0:
                maze[i][j] += maze[i][j-1]
        elif j == 0:
            maze[i][j] += maze[i-1][j]
        else:
            maze[i][j] += max(maze[i-1][j], maze[i][j-1])

print(maze[n-1][m-1])
