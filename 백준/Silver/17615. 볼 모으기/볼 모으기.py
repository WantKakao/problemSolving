n = int(input())
balls = [*map(str, input())]

arr = []
temp = 1
for i in range(n-1):
    if balls[i] != balls[i+1]:
        arr.append(temp)
        temp = 1
    else:
        temp += 1
arr.append(temp)
red_arr = arr[::2]
blue_arr = arr[1::2]

# 양쪽 끝 공 색깔이 다른 경우
if len(red_arr) == len(blue_arr):
    red_left = sum(red_arr) - red_arr[0]
    blue_right = sum(blue_arr) - blue_arr[-1]
    ans = min(red_left, blue_right)
# 양쪽 끝 공 색깔이 같은 경우
else:
    red_left = sum(red_arr) - red_arr[0]
    red_right = sum(red_arr) - red_arr[-1]
    blue = sum(blue_arr)
    ans = min(red_left, red_right, blue)

print(ans)