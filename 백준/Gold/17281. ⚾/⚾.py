from itertools import permutations

def simulate(order, innings):
    score = 0
    idx = 0
    for inning in innings:
        base1, base2, base3 = 0, 0, 0
        outs = 0
        while outs < 3:
            hit = inning[order[idx]]
            if hit == 0:
                outs += 1
            elif hit == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif hit == 2:
                score += base2 + base3
                base1, base2, base3 = 0, 1, base1
            elif hit == 3:
                score += base1 + base2 + base3
                base1, base2, base3 = 0, 0, 1
            else:  # 홈런
                score += base1 + base2 + base3 + 1
                base1, base2, base3 = 0, 0, 0
            idx = (idx + 1) % 9
    return score

n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]

max_score = 0
for p in permutations(range(1, 9)):
    order = list(p[:3]) + [0] + list(p[3:])
    max_score = max(max_score, simulate(order, innings))

print(max_score)