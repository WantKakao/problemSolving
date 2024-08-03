n = int(input())
A = B = 100

for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        continue
    elif a > b:
        B -= a
    else:
        A -= b

print(A)
print(B)