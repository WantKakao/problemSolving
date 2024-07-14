import sys
input = sys.stdin.readline

i = 1
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    a, b = divmod(V, P)
    print(f"Case {i}: {L * a + min(L, b)}")
    i += 1