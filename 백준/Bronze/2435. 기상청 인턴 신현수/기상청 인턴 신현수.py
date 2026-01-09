n, k = map(int, input().split())
l = list(map(int, input().split()))
ans = -10000
for i in range(n-k+1):
    ans = max(ans, sum(l[i:i+k]))
    
print(ans)