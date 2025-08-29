import sys
input = sys.stdin.readline

N = int(input().strip())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

# 초기 카드 배열: 0..N-1
arr = list(range(N))

def check(arr):
    # 위치 i에 있는 카드 arr[i]가 플레이어 i%3 에게 가는데,
    # 그 카드의 원하는 플레이어가 P[arr[i]] 와 같아야 함
    for i, card in enumerate(arr):
        if P[card] != i % 3:
            return False
    return True

# 0번 섞기(초기 상태)부터 검사
if check(arr):
    print(0)
    sys.exit(0)

seen = set()
seen.add(tuple(arr))

count = 0
while True:
    # 한 번 섞기
    tmp = [0] * N
    for i in range(N):
        tmp[S[i]] = arr[i]
    arr = tmp
    count += 1

    if tuple(arr) in seen:
        print(-1)
        break
    seen.add(tuple(arr))

    if check(arr):
        print(count)
        break
