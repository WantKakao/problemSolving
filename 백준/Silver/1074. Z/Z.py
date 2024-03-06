N, r, c = map(int, input().split())
num = 2**N
answer = 0
temp = (num**2) // 4
while True:
    if r >= num//2:
        answer += 2*temp
        r -= num//2
    if c >= num//2:
        answer += temp
        c -= num//2
    if temp == 1:
        break
    else:
        num //= 2
        temp //= 4
print(answer)