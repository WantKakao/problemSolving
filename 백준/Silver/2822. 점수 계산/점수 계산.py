score = []
for idx in range(8):
    score.append((int(input()), idx+1))
score.sort()
S = 0
N = []
for idx in range(3, 8):
    S += score[idx][0]
    N.append(str(score[idx][1]))
N.sort()
print(S)
print(' '.join(N))