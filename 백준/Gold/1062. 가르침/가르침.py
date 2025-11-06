from itertools import combinations

n, k = map(int, input().split())
words = [input() for _ in range(n)]

if k < 5:
    print(0)
    exit()
if k == 26:
    print(n)
    exit()
    
essential = ['a', 'c', 'i', 'n', 't']
essential_masked = 0
for c in essential:
    essential_masked |= (1 << (ord(c) - ord('a')))

masked_words = []
for w in words:
    base = 0
    for c in w[4:-4]:
        base |= (1 << (ord(c) - ord('a')))
    masked_words.append(base)

alphabets = [chr(i + ord('a')) for i in range(26) if chr(i + ord('a')) not in essential]
ans = 0
for comb in combinations(alphabets, k-5):
    masked = essential_masked
    for c in comb:
        masked |= (1 << (ord(c) - ord('a')))
    count = 0
    for w in masked_words:
        if (masked & w) == w:
            count += 1
    ans = max(ans, count)
print(ans)