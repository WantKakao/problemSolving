t = int(input())

for _ in range(t):
    A, B = 0 ,0
    for _ in range(9):
        a, b = map(int, input().split())
        A += a
        B += b
    if A > B:
        print("Yonsei")
    elif A < B:
        print("Korea")
    else:
        print("Draw")