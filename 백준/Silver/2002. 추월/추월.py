import sys
input = sys.stdin.readline

n = int(input())
l = []
l2 = []
ans = 0
for _ in range(n):
    l.append(input().rstrip())
for _ in range(n):
    l2.append(input().rstrip())
for i in range(n):
    p = l[:i]
    for j in p:
        idx = l2.index(l[i])
        if j in l2[idx:]:
            ans += 1
            break
print(ans)