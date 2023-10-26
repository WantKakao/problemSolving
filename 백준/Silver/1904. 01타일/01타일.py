n = int(input())
ans = [0 for _ in range(1000001)]
ans[0] = 0
ans[1] = 1
ans[2] = 2
for i in range(3, 1000001):
    ans[i] = (ans[i-2] + ans[i-1])%15746
print(ans[n])