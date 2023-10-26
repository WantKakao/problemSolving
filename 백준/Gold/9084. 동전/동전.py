test = int(input())
for _ in range(test):
    coin = int(input())
    coins = [*map(int, input().split())]
    ans = int(input())

    possible = [0 for _ in range(ans+1)]
    for c in coins:
        if c <= ans:
            possible[c] += 1
            for i in range(1, ans+1-c):
                possible[i+c] += possible[i]

    print(possible[-1])