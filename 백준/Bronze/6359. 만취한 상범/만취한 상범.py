import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    num_of_div = [1 for _ in range(n+1)]
    for num in range(2, n+1):
        for divisor in range(2, num+1):
            if num % divisor == 0:
                num_of_div[num] += 1

    ans = 0
    for i in range(1, n+1):
        if num_of_div[i] % 2 == 1:
            ans += 1
    print(ans)