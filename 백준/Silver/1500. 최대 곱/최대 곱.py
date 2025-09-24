s, k = map(int, input().split())
n, m = divmod(s, k)
ans = (n+1)**(m) * n**(k-m)
print(ans)