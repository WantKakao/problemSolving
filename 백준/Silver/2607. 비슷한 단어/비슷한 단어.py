import sys
input = sys.stdin.readline

n = int(input())
word = list(input().rstrip())
word.sort()
ans = 0
w = len(word)

for _ in range(n-1):
    word2 = list(input().rstrip())
    word2.sort()
    w2 = len(word2)

    if w == w2-1:
        for i in range(65, 91):
            word3 = word + [chr(i)]
            word3.sort()
            if word3 == word2:
                ans += 1
                break

    elif w == w2:
        if word == word2:
            ans += 1
        else:
            flag = 0
            for i in range(w):
                for j in range(65, 91):
                    word3 = word[:i] + [chr(j)] + word[i+1:]
                    word3.sort()
                    if word3 == word2:
                        ans += 1
                        flag = 1
                        break
                if flag:
                    break

    elif w == w2+1:
        for i in range(65, 91):
            word3 = word2 + [chr(i)]
            word3.sort()
            if word3 == word:
                ans += 1
                break

print(ans)