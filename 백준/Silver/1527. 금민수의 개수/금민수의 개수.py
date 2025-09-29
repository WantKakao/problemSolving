from itertools import product

arr = [4, 7]
nums = []
for k in range(1, 10):
    temp = product(arr, repeat=k)
    for t in temp:
        s = ''.join(map(str, t))
        nums.append(int(s))
        
a, b = map(int, input().split())
ans = 0
for n in nums:
    if a <= n <= b:
        ans += 1
        
print(ans)