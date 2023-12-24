import sys
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())
k = int(input())
relative = [[] for _ in range(n+1)]
for _ in range(k):
    parent, child = map(int, input().split())
    relative[child].append(parent)

x_parents = [x]
y_parents = [y]
while 1:
    if len(relative[x]):
        x_parents.append(relative[x][0])
        x = relative[x][0]
    if len(relative[y]):
        y_parents.append(relative[y][0])
        y = relative[y][0]
    if len(relative[x]) + len(relative[y]) == 0:
        break

def ans():
    for i in x_parents:
        for j in y_parents:
            if i == j:
                a = x_parents.index(i)
                b = y_parents.index(j)
                print(a + b)
                return True
    print(-1)
    return False

ans()
