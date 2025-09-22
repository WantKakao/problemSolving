m, n = map(int, input().split())
if m < n:
    a = (m+1) // 2 - 1
    b = m // 2 if m % 2 == 0 else n - (m+1) // 2
if m == n:
    a = (m+1) // 2 - 1
    b = n // 2
if m > n:
    a = (n-1) // 2 if n % 2 == 0 else m - (n+1) // 2
    b = n // 2

print(a, b)