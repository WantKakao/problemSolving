n = int(input())
k = 3
for _ in range(n-1):
    k += (k-1)
    
print(k*k)