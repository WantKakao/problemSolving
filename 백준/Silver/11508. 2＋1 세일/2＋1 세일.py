import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
l.sort(reverse=True)
ans = 0
for i in range(n):
    if i % 3 != 2:
        ans += l[i]
print(ans)