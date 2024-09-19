t = int(input())
for _ in range(t):
    n, s = map(str, input().split())
    new_s = s[:int(n)-1] + s[int(n):]
    print(new_s)