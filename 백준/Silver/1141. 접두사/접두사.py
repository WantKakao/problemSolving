n = int(input())
S = set()
for _ in range(n):
    S.add(input())

def check_set(S):
    s = len(S)
    list_S = list(S)
    prefix = [-1 for _ in range(s)]
    for i in range(s):
        word = list_S[i]
        w = len(word)
        for j in range(s):
            if w <= len(list_S[j]) and word == list_S[j][:w]:
                prefix[i] += 1
    for k in range(s-1, -1, -1):
        if prefix[k]:
            list_S.pop(k)
    return len(list_S)

print(check_set(S))
        