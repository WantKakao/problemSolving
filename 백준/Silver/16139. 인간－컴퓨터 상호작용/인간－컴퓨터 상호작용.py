word = input()
n = int(input())
for _ in range(n):
    w, a, b = map(str, input().split())
    a, b = map(int, (a, b))
    ans = 0
    for i in range(a, b+1):
        if word[i] == w:
            ans += 1
    print(ans)