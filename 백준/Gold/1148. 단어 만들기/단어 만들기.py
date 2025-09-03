import sys
input = sys.stdin.readline

dictionary = []
while True:
    S = input().strip()
    if S == '-':
        break
    cnt = [0]*26
    for s in S:
        cnt[ord(s)-65] += 1
    dictionary.append(cnt)

while True:
    B = input().strip()
    if B == '#':
        break
    bcnt = [0]*26
    for b in B:
        bcnt[ord(b)-65] += 1
    alphabet_idx = [i for i,v in enumerate(bcnt) if v>0]

    count = [0]*26
    # dictionary 전체를 한 번만 순회
    for d in dictionary:
        ok = True
        for i in range(26):
            if d[i] > bcnt[i]:
                ok = False
                break
        if not ok: 
            continue
        # d 단어가 가능하면, 포함된 알파벳에 대해 카운트
        for i in alphabet_idx:
            if d[i] > 0:
                count[i] += 1

    c_count = [count[i] for i in alphabet_idx]
    m, M = min(c_count), max(c_count)

    for i in alphabet_idx:
        if count[i] == m:
            print(chr(i+65), end='')
    print(f' {m} ', end='')
    for i in alphabet_idx:
        if count[i] == M:
            print(chr(i+65), end='')
    print(f' {M}')
