a, b = map(int, input().split())
n = int(input())
ans = abs(b-a)
for _ in range(n):
    l = int(input())
    ans = min(ans, abs(l-b)+1)
    
print(ans)