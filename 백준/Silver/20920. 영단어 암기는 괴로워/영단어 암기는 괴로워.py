import sys
input = sys.stdin.readline
n, m = map(int, input().split())
words = dict()
for _ in range(n):
    w = input().rstrip()
    if len(w) < m:
        continue
    if w in words.keys():
        words[w] += 1
    else:
        words[w] = 1
arr = [(c, w) for w, c in words.items()]
arr.sort(key=lambda x: (-x[0], -len(x[1]), x[1]))
for i in arr:
    print(i[1])
