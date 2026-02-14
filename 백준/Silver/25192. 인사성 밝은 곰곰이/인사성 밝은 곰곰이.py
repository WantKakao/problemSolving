import sys
input = sys.stdin.readline
n = int(input())
ans = 0
for _ in range(n):
    s = input().rstrip()
    if s == 'ENTER':
        d = dict()
    else:
        if d.get(s) is None:
            d[s] = 1
            ans += 1
        else:
            pass
print(ans)