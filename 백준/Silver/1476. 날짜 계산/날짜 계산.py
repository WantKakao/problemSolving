E, S, M = map(int, input().split())

while True:
    if E == S == M:
        print(E)
        break
    if E <= S and E <= M:
        E += 15
    elif S <= E and S <= M:
        S += 28
    else:
        M += 19
