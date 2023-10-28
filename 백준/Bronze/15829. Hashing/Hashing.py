n = int(input())
s = input()
ans = 0
for i in range(n):
    k = ord(s[i])-96
    ans += k * (31**i)
print(ans)