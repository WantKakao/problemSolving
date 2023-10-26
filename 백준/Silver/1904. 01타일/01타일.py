n = int(input())
# ans = [0 for _ in range(1000001)]
ans = [0, 0, 0]
# ans[0] = 0
ans[1] = 1
ans[2] = 2
# for i in range(3, 1000001):
#     ans[i] = (ans[i-2] + ans[i-1])%15746
# print(ans[n])
if n == 1 or n == 2:
    print(ans[n])
else:
    for i in range(n-2):
        ans[0], ans[1] = ans[1], ans[2]
        ans[2] = (ans[0] + ans[1]) % 15746
    print(ans[2])