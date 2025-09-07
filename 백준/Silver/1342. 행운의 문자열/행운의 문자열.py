from collections import Counter

s = input()
n = len(s)
counter = Counter(s)   # 각 글자 개수 세기
ans = 0

def backtrack(path, prev):
    global ans
    if len(path) == n:   # 길이 다 채웠으면 유효한 순열 완성
        ans += 1
        return

    for ch in counter:
        if counter[ch] > 0 and ch != prev:  # 연속된 글자 방지
            counter[ch] -= 1
            backtrack(path + ch, ch)
            counter[ch] += 1

backtrack("", None)
print(ans)