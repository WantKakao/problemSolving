import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = dict()
ans = n

for _ in range(n):
    w = input().rstrip()
    words[w] = 1

for _ in range(m):
    ws = [*map(str, input().rstrip().split(','))]
    for w in ws:
        if w in words.keys():
            if words[w] == 1:
                words[w] = 0
                ans -= 1
    print(ans)
