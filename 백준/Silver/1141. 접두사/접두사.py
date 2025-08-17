n = int(input())
S = []
for _ in range(n):
    S.append(input())

def check_set(S):
    s = len(S)
    prefix = [-1 for _ in range(s)]
    for i in range(s):
        word = S[i]
        w = len(word)
        for j in range(s):
            if w <= len(S[j]) and word == S[j][:w]:
                prefix[i] += 1
    return prefix

while True:
    P = check_set(S)
    if sum(P) == 0:
        break
    p = P.index(max(P))
    S.pop(p)
print(len(P))
        