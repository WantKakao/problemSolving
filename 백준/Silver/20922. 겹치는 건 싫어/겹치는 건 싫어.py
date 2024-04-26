n, k = map(int, input().split())
sequence = [*map(int, input().split())]

arr = [0 for _ in range(100001)]
i, j, ans = 0, 0, 0
while j < n:
    arr[sequence[j]] += 1
    if arr[sequence[j]] > k:
        while sequence[i] != sequence[j]:
            arr[sequence[i]] -= 1
            i += 1
        arr[sequence[i]] -= 1
        i += 1
    ans = max(ans, j-i+1)
    j += 1

print(ans)