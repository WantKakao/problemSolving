from itertools import combinations

n, k = map(int, input().split())
words = [input().strip() for _ in range(n)]

# 기본 글자
essential = {'a', 'n', 't', 'i', 'c'}

# 예외 처리
if k < 5:
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

# 단어를 비트마스크로 변환
word_masks = []
for w in words:
    mask = 0
    for c in set(w[4:-4]):  # "anta", "tica" 제거
        mask |= (1 << (ord(c) - ord('a')))
    word_masks.append(mask)

# 기본 배운 글자 비트
learned_mask = 0
for c in essential:
    learned_mask |= (1 << (ord(c) - ord('a')))

# 가능한 알파벳 리스트 (a, n, t, i, c 제외)
alphabets = [chr(i + ord('a')) for i in range(26) if chr(i + ord('a')) not in essential]

max_count = 0

# 나머지 알파벳 중에서 k-5개 선택
for comb in combinations(alphabets, k - 5):
    cur_mask = learned_mask
    for c in comb:
        cur_mask |= (1 << (ord(c) - ord('a')))
    # 읽을 수 있는 단어 수 세기
    count = 0
    for w_mask in word_masks:
        if (w_mask & cur_mask) == w_mask:
            count += 1
    max_count = max(max_count, count)

print(max_count)
