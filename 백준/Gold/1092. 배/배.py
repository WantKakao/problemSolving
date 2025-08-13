n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
    exit()

positions = [0] * n  # 각 크레인이 현재 가리키는 박스 인덱스
checked = [False] * m
count = 0
remain = m

while remain > 0:
    for i in range(n):
        while positions[i] < m:
            if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                remain -= 1
                break
            positions[i] += 1
    count += 1

print(count)
