S = []
for _ in range(5):
    a, b, c, d = map(int, input().split())
    S.append(a+b+c+d)
print(S.index(max(S))+1, max(S))