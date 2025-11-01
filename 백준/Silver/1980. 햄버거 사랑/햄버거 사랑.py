x, y, t = map(int, input().split())
n, m = min(x, y), max(x, y)
a, b = t//n, t%n
ans1, ans2 = a, b
for i in range(a-1, -1, -1):
    remain = t-(i*n)
    new_sum = remain//m + i
    new_remain = remain%m
    if new_remain < ans2:
        ans2 = new_remain
        ans1 = new_sum
        
print(ans1, ans2)