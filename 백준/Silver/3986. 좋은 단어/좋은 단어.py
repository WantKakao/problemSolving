import sys
input = sys.stdin.readline

ans = 0
t = int(input())
for _ in range(t):
    word = input().rstrip()
    q = []
    is_good = True
    for w in word:
        if not q or q[-1] != w:
            q.append(w)
        elif q[-1] == w:
            q.pop()
        else:
            is_good = False
            break

    if is_good and not q:
        ans += 1

print(ans)