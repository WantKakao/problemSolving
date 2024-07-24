import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# dp[i][j]는 nums[i:j+1]이 회문이면 True, 아니면 False
dp = [[False] * n for _ in range(n)]

# 길이 1인 경우, 모든 단일 문자 서브어레이는 회문입니다.
for i in range(n):
    dp[i][i] = True

# 길이 2인 경우를 처리합니다.
for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = True

# 길이 3 이상인 경우를 처리합니다.
for length in range(3, n+1):  # length는 부분 배열의 길이
    for i in range(n-length+1):
        j = i + length - 1
        if nums[i] == nums[j] and dp[i+1][j-1]:
            dp[i][j] = True

q = int(input())
results = []
for _ in range(q):
    s, e = map(int, input().split())
    results.append(1 if dp[s-1][e-1] else 0)

print('\n'.join(map(str, results)))
