import sys
input = sys.stdin.readline

n, m = map(int, input().split())
req = [[] for _ in range(n+1)]
revReq = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    req[b].append(a)
    revReq[a].append(b)

ans = [-1 for _ in range(n+1)]
t = 1
count = 0
while 1:
    if count == n:
        break
    temp = []
    for i in range(1, n+1):
        if not req[i] and ans[i] == -1:
            ans[i] = t
            temp.append(i)
            count += 1
    for i in temp:
        for r in revReq[i]:
            req[r].remove(i)
    t += 1

for k in range(1, n+1):
    print(ans[k], end=' ')