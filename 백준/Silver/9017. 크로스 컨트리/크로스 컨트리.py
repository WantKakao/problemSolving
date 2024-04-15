import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    team = [*map(int, input().split())]

    M = max(team)
    six_man_team = []
    for i in range(1, M+1):
        if team.count(i) == 6:
            six_man_team.append(i)

    arr = [[] for _ in range(M+1)]
    rank = 1
    for t in team:
        if t in six_man_team:
            arr[t].append(rank)
            rank += 1

    fifth_rank = 1000
    score = 4000
    winner = 0
    for i in range(1, M+1):
        if i in six_man_team:
            if sum(arr[i][:4]) < score:
                winner = i
                score = sum(arr[i][:4])
                fifth_rank = arr[i][4]
            elif sum(arr[i][:4]) == score and arr[i][4] < fifth_rank:
                winner = i
                fifth_rank = arr[i][4]

    print(winner)