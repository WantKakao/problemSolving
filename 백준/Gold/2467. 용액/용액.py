n = int(input())
liquid = list(map(int, input().split()))

ans = liquid[0] + liquid[n-1]
pair1, pair2 = liquid[0], liquid[n-1]

for l in liquid:
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        temp = l + liquid[mid]

        if abs(temp) < abs(ans) and l != liquid[mid]:
            ans = temp
            pair1, pair2 = l, liquid[mid]
            
        if temp < 0:
            start = mid + 1
        else:
            end = mid - 1

print(min(pair1, pair2), max(pair1, pair2))