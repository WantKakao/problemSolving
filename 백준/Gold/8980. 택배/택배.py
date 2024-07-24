import sys

input = sys.stdin.readline

# 입력 처리
N, C = map(int, input().split())
M = int(input())
parcel = []
for _ in range(M):
    parcel.append([*map(int, input().split())])

# 도착 마을 기준으로 정렬
parcel.sort(key=lambda x: x[1])

# 각 마을의 트럭 적재 상태를 관리하는 배열
current_load = [0] * (N + 1)
total_boxes = 0

for send, receive, num in parcel:
    # 트럭이 현재 경로에서 실을 수 있는 최대 용량을 확인
    max_load_at_send = max(current_load[send:receive])
    load_capacity = C - max_load_at_send
    load_to_add = min(num, load_capacity)

    if load_to_add > 0:
        for i in range(send, receive):
            current_load[i] += load_to_add
        total_boxes += load_to_add

# 결과 출력
print(total_boxes)
