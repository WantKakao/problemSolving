import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = dict()
for _ in range(n):
    site, pwd = map(str, input().rstrip().split())
    memo[site] = pwd
for _ in range(m):
    site = input().rstrip()
    print(memo[site])
