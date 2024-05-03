import sys
input = sys.stdin.readline

n = int(input())
expect_rank = []
for _ in range(n):
    expect_rank.append(int(input()))

expect_rank.sort()
answer = 0
for i in range(n):
    answer += abs(expect_rank[i] - (i+1))

print(answer)