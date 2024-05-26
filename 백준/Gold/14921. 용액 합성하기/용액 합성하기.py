n = int(input())
solution = list(map(int, input().split()))

ans = 2e9
for i in range(n):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        temp = solution[i] + solution[mid]
        if abs(temp) < abs(ans) and i != mid:
            ans = temp

        if temp < 0:
            start = mid + 1
        elif temp > 0:
            end = mid - 1
        else:
            break

print(ans)