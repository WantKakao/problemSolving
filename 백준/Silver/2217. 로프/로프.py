import sys
input = sys.stdin.readline

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort()
ans = 0
for i in range(n):
    temp = rope[i] * (n-i)
    if temp > ans:
        ans = temp

print(ans)