S = input()
l = [0 for _ in range(26)]
for s in S:
    l[ord(s)-97] += 1
for i in l:
    print(i, end=' ')