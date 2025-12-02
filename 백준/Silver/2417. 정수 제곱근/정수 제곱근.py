n = int(input())
k = int(n ** 0.5)
if k ** 2 >= n:
    print(k)
else:
    print(k+1)