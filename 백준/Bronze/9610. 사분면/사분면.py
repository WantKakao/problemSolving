n = int(input())
q = [0, 0, 0, 0, 0]
for _ in range(n):
    a, b = map(int, input().split())
    if a == 0 or b == 0:
        q[0] += 1
    elif a > 0 and b > 0:
        q[1] += 1
    elif a < 0 < b:
        q[2] += 1
    elif a < 0 and b < 0:
        q[3] += 1
    else:
        q[4] += 1

for i in range(1, 5):
    print(f"Q{i}: {q[i]}")
print(f"AXIS: {q[0]}")