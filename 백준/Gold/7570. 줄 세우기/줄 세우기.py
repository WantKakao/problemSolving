def solve(n, children):
    # 각 숫자의 위치를 저장
    positions = {num: i for i, num in enumerate(children)}
    visited = [False for _ in range(n+1)]
    # 연속된 숫자들의 최대 길이를 찾음
    max_len = 0
    for start in range(1, n + 1):
        if not visited[start]:
            visited[start] = True
            current_len = 1
            current = start
            while current + 1 in positions and positions[current + 1] > positions[current]:
                current += 1
                visited[current] = True
                current_len += 1
            max_len = max(max_len, current_len)

    # 이동해야 할 어린이 수 반환
    return n - max_len


# 입력 받기
n = int(input())
children = list(map(int, input().split()))

# 결과 출력
print(solve(n, children))