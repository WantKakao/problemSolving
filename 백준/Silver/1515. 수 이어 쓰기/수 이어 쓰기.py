num = input()
idx = 0
n = 1
l = len(num)
while idx < l:
    for a in str(n):
        if idx == l:
            break
        if a == num[idx]:
            idx += 1
    n += 1

print(n-1)