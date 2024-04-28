import copy

n = int(input())
start = [*map(int, input())]
end = [*map(int, input())]

# start2 = 첫번째 전구를 조작한 후의 start 배열
start2 = copy.deepcopy(start)
start2[0] = 1 if start2[0] == 0 else 0
start2[1] = 1 if start2[1] == 0 else 0

ans, ans2 = 0, 1
for i in range(n-1):
    if start[i] != end[i]:
        ans += 1
        start[i] = 1 if start[i] == 0 else 0
        start[i+1] = 1 if start[i+1] == 0 else 0
        if i+2 < n:
            start[i+2] = 1 if start[i+2] == 0 else 0

    if start2[i] != end[i]:
        ans2 += 1
        start2[i] = 1 if start2[i] == 0 else 0
        start2[i+1] = 1 if start2[i+1] == 0 else 0
        if i + 2 < n:
            start2[i+2] = 1 if start2[i+2] == 0 else 0

if start == end:
    print(ans)
elif start2 == end:
    print(ans2)
else:
    print(-1)