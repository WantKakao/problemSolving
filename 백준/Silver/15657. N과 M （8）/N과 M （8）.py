n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()


def permu(x, c, arr):
    if c == m:
        for a in arr:
            print(a, end=' ')
        print()
        return
    for j in range(x, n):
        permu(j, c+1, arr+[nums[j]])


permu(0, 0, [])
