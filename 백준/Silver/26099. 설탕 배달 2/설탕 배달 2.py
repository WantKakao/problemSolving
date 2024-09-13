n  = int(input())
k = n // 15
m = n % 15
arr = [0, 1, 2, 1, 2, 1, 2, 3, 2, 3, 2, 3, 4, 3, 4]
if n==1 or n==2 or n==4 or n==7:
    print(-1)
else:
    print(k*3 + arr[m])