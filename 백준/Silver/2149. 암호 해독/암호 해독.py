k = list(input())
s = input()
lk = len(k)
ls = len(s)
l = ls // lk
ans = ['' for _ in range(ls)]
k2 = sorted(k)
arr = []
for i in range(lk):
    for j in range(lk):
        if k2[i] == k[j]:
            arr.append(j)
            k[j] = -1

for i in range(lk):
    for j in range(l):
        ans[arr[i]+(j*lk)] = s[(i*l)+j]
print(''.join(ans))