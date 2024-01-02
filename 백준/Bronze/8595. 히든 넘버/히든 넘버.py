import sys

n = int(input())
word = [*map(str, sys.stdin.readline().rstrip())]

# print(word)
ans = '0'
real_ans = 0
for i in range(len(word)):
    if word[i].isdecimal():
        ans += word[i]
    else:
        real_ans += int(ans)
        ans = '0'
real_ans += int(ans)
print(real_ans)
