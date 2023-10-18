import sys
input = sys.stdin.readline

n = int(input())
top = [*map(int, input().split())]
stack = [[0, top[0]]]
ans = [0]

for i in range(1, n):
    while stack:
        if top[i] > stack[-1][1]:
            stack.pop()
        else:
            break
    ans.append(stack[-1][0] + 1) if stack else ans.append(0)
    stack.append([i, top[i]])

print(*ans)
