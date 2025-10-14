r, c = map(int, input().split())
words = []
for _ in range(r):
    words.append(list(map(str, input())))

dic = []
for i in range(r):
    start = 0
    for j in range(c):
        if words[i][j] == '#':
            if j >= 2 and words[i][j-1] != '#' and words[i][j-2] != '#':
                dic.append("".join(words[i][start:j]))
            start = j+1
    if words[i][c-2] != '#' and words[i][c-1] != '#':
        dic.append("".join(words[i][start:]))
        
for j in range(c):
    start = 0
    for i in range(r):
        if words[i][j] == '#':
            if i >= 2 and words[i-1][j] != '#' and words[i-2][j] != '#':
                dic.append("".join(row[j] for row in words[start:i]))
            start = i+1
    if words[r-2][j] != '#' and words[r-1][j] != '#':
        dic.append("".join(row[j] for row in words[start:]))

dic.sort()
print(dic[0])