import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

time = 0
while time <= 100:
    # check A[r][c]
    if 0 <= r-1 < len(A) and 0 <= c-1 < len(A[0]) and A[r-1][c-1] == k:
        print(time)
        break

    row = len(A)
    col = len(A[0])
    L = 0

    if row >= col:
        for i in range(row):
            temp = []
            for j in range(col):
                if A[i][j] == 0:
                    continue
                found = False
                for t in temp:
                    if A[i][j] == t[1]:
                        t[0] += 1
                        found = True
                        break
                if not found:
                    temp.append([1, A[i][j]])
            temp.sort()
            if 100 >= 2*len(temp) > L:
                L = 2*len(temp)
            A[i] = []
            for a, n in temp:
                A[i].append(n)
                A[i].append(a)
        for i in range(row):
            dif = L - len(A[i])
            for _ in range(dif):
                A[i].append(0)
            A[i] = A[i][:100]

    else:
        B = [[] for _ in range(col)]
        for j in range(col):
            temp = []
            for i in range(row):
                if A[i][j] == 0:
                    continue
                found = False
                for t in temp:
                    if A[i][j] == t[1]:
                        t[0] += 1
                        found = True
                        break
                if not found:
                    temp.append([1, A[i][j]])
            temp.sort()
            if 2 * len(temp) > L:
                L = 2 * len(temp)
            for a, n in temp:
                B[j].append(n)
                B[j].append(a)
        for j in range(col):
            dif = L - len(B[j])
            for _ in range(dif):
                B[j].append(0)
        A = [[0 for _ in range(len(B))] for _ in range(len(B[0]))]
        for i in range(len(B[0])):
            for j in range(len(B)):
                A[i][j] = B[j][i]
        for i in range(len(A)):
            A[i] = A[i][:100]

    time += 1

if time > 100:
    print(-1)
