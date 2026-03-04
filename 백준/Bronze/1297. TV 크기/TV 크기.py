x, a, b = map(int, input().split())
T = x**2 / (a**2 + b**2)
t = T ** 0.5
print(int(t*a), int(t*b))