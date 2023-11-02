n = int(input())

arr = [1,3,5]
if n <= 3:
    print(arr[n-1])
else:
    for _ in range(n-3):
        temp = (2 * arr[1] + arr[2]) % 10007
        arr.pop(0)
        arr.append(temp)
    print(arr[2])