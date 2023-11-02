n = int(input())
arr = [1, 1, 2]
if n <= 3:
    print(arr[n-1])
else:
    for _ in range(n-3):
        temp = arr[1] + arr[2]
        arr.pop(0)
        arr.append(temp)
    print(arr[2])
