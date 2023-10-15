n = int(input())
arr = set()
for _ in range(n):
    arr.add(input())
arr = list(arr)
arr.sort(key = lambda x: (len(x), x))
for i in arr:
    print(i)