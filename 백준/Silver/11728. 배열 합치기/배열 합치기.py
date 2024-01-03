import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []

i = j = 0
while i < a or j < b:
    if i == a or j == b:
        if i == a:
            C.append(B[j])
            j += 1
        else:
            C.append(A[i])
            i += 1
    elif A[i] <= B[j]:
        C.append(A[i])
        i += 1
    else:
        C.append(B[j])
        j += 1

for i in C[:-1]:
    print(i, end=' ')
print(C[-1])
