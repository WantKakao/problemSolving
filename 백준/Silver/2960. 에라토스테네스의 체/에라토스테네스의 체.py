import sys
input = sys.stdin.readline

N, K = map(int, input().split())
erased = [False for _ in range(N+1)]
n = 0
for i in range(2, N+1):
    if not erased[i]:
        for j in range(i, N+1, i):
            if not erased[j]:
                erased[j] = True
                n += 1
                if n == K:
                    print(j)