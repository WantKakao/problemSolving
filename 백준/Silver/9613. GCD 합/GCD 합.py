import sys
input = sys.stdin.readline

def GCD(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    if a > b:
        a %= b
    else:
        b %= a
    return GCD(a, b)

t = int(input())
for _ in range(t):
    temp = [*map(int, input().split())]
    N = temp[0]
    nums = temp[1:]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += GCD(nums[i], nums[j])
    print(ans)