import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    k = int(input())
    ans += k
ans -= n-1
print(ans)