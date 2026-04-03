import sys
input = sys.stdin.readline

n = int(input())
c = [[i+1, 0, 0, 0] for i in range(3)]
for _ in range(n):
    s1, s2, s3 = map(int, input().split())
    c[0][s1] += s1
    c[1][s2] += s2
    c[2][s3] += s3
c.sort(key=lambda x: (-sum(x)+x[0], -x[3], -x[2]))
if sum(c[0])-c[0][0] == sum(c[1])-c[1][0] and c[0][3] == c[1][3] and c[0][2] == c[1][2]:
    print(0, sum(c[0])-c[0][0])
else:
    print(c[0][0], sum(c[0])-c[0][0])