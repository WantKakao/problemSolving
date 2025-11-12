import sys

n = int(input())
nums = list(map(int, input().split()))

def iqtest(n, a, b):
    for i in range(1, n):
        if nums[i-1]*a+b != nums[i]:
            return False
    return True
        
if n == 1:
    print('A')
    sys.exit()
    
p = 0
ans = 'A'
for a in range(-200, 201):
    b = nums[1] - nums[0]*a
    if iqtest(n, a, b) and nums[n-1]*a+b != ans:
        p += 1
        ans = nums[n-1]*a+b

if p == 0:
    print('B')
elif p == 1:
    print(ans)
else:
    print('A')