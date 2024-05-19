n, score, max_rank = map(int, input().split())
if n == 0:
    print(1)
else:
    rank = list(map(int, input().split()))

    i = 0
    temp = 0
    while i < n:
        if temp == 0 and rank[i] == score:
            temp = i+1
        if rank[i] < score:
            break
        i += 1

    if i < max_rank:
        if temp != 0:
            print(temp)
        else:
            print(i+1)
    else:
        print(-1)