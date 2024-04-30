import sys
input = sys.stdin.readline

n, max_weight = map(int, input().split())
arr = []
for _ in range(n):
    weight, happiness, quantity = map(int, input().split())
    i = 0
    while 2**i < quantity:
        arr.append((weight*(2**i), happiness*(2**i)))
        quantity -= 2**i
        i += 1
    arr.append((weight*quantity, happiness*quantity))

dp = [0 for _ in range(max_weight+1)]
for w, h in arr:
    temp = [0 for _ in range(max_weight+1)]
    for i in range(w):
        temp[i] = dp[i]
    for i in range(w, max_weight+1):
        temp[i] = max(dp[i], dp[i-w]+h)
    dp = temp

print(dp[-1])