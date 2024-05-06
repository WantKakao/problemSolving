n = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = 1e9
for i in range(n):
    temp = arr[i] + arr[2*n-1-i]
    if temp < ans:
        ans = temp

print(ans)