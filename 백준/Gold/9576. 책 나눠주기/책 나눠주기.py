import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    want_book = []
    for _ in range(M):
        a, b = map(int, input().split())
        want_book.append((a, b))
    
    # 끝나는 책 번호 b 기준으로 정렬
    want_book.sort(key=lambda x: x[1])
    
    allocated = [False] * (N + 1)  # 책 번호가 1부터 시작하므로 N+1개
    count = 0
    
    for a, b in want_book:
        for i in range(a, b + 1):
            if not allocated[i]:
                allocated[i] = True
                count += 1
                break
    
    print(count)
