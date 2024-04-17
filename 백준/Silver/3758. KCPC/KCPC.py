import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    teams, probs, my_idx, m = map(int, input().split())
    arr = [[0 for _ in range(probs+2)] for _ in range(teams+1)]
    for order in range(m):
        idx, prob, score = map(int, input().split())
        arr[idx][prob] = max(arr[idx][prob], score)
        arr[idx][0] += 1
        arr[idx][-1] = order

    attempt, last, total = arr[my_idx][0], arr[my_idx][-1], sum(arr[my_idx][1:probs+1])
    ans = 1
    for i in range(1, teams+1):
        if total < sum(arr[i][1:probs+1]):
            ans += 1
        elif total > sum(arr[i][1:probs+1]):
            continue
        else:
            if attempt > arr[i][0]:
                ans += 1
            elif attempt < arr[i][0]:
                continue
            else:
                if last > arr[i][-1]:
                    ans += 1
                else:
                    continue

    print(ans)