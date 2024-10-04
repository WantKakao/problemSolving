t = int(input())
for _ in range(t):
    total = 0
    score = 0
    n = int(input())
    for _ in range(n):
        a, b = map(float, input().split())
        total += a
        score += b*a
    print(int(total), round(score / total, 1))