import sys
input = sys.stdin.readline

dictionary = []
while True:
    S = input().strip()
    if S == '-':
        break
    temp = [0 for _ in range(26)]
    for s in S:
        temp[ord(s)-65] += 1
    dictionary.append(temp)

def check_alphabet(word):
    for i in range(26):
        if word[i] > temp[i]:
            return
    for idx in alphabet_idx:
        if word[idx] > 0:
            count[idx] += 1
    return

while True:
    B = input().strip()
    if B == '#':
        break
    temp = [0 for _ in range(26)]
    for b in B:
        temp[ord(b)-65] += 1
    alphabet_idx = [i for i, v in enumerate(temp) if v > 0]
    count = [0 for _ in range(26)]
    for d in dictionary:
        check_alphabet(d)
    c_count = [v for i, v in enumerate(count) if i in alphabet_idx]
    m, M = min(c_count), max(c_count)
    for i in range(26):
        if count[i] == m and i in alphabet_idx:
            print(chr(i+65), end='')
    print(' ', end='')
    print(m, end=' ')
    for i in range(26):
        if count[i] == M and i in alphabet_idx:
            print(chr(i+65), end='')
    print(' ', end='')
    print(M)