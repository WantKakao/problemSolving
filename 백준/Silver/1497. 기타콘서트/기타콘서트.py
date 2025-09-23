from itertools import combinations

n, m = map(int, input().split())
song = []
for _ in range(n):
    g, s = map(str, input().split())
    song.append(s)

p = 0
ans = -1
for i in range(1, n+1):
    comb = combinations(song, i)
    for c in comb:
        temp = [0 for _ in range(m)]
        for k in range(i):
            for j in range(m):
                if c[k][j] == 'Y':
                    temp[j] = 1
        if sum(temp) > p:
            p = sum(temp)
            ans = i
        
print(ans)