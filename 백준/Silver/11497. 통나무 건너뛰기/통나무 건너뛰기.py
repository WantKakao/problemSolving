import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    woods = list(map(int, input().split()))
    woods.sort()
    maximum = 0
    for i in range(2, n, 2):
        temp = woods[i] - woods[i-2]
        if temp > maximum:
            maximum = temp
    for j in range(3, n, 2):
        temp = woods[j] - woods[j - 2]
        if temp > maximum:
            maximum = temp
    print(maximum)