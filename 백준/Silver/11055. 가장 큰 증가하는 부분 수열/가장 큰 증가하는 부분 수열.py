n = int(input())
arr = list(map(int, input().split()))

temp_sum = 0
arr_sum = [arr[i] for i in range(n)]
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            arr_sum[i] = max(arr_sum[i], arr_sum[j]+arr[i])

print(max(arr_sum))