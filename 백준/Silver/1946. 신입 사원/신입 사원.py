import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n = int(input())
    grade = []
    for _ in range(n):
        x, y = map(int, input().split())
        grade.append((x, y))
    m, cnt = n+1, 0
    grade.sort(reverse=True)
    while grade:
        a, b = grade.pop()
        if b < m:
            m = b
            cnt += 1
    print(cnt)