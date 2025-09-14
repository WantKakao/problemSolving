n = int(input())
dice = list(map(int, input().split()))
d = sum(dice)

m1 = min(dice)

m2_faces = []
for i in range(6):
    for j in range(i+1, 6):
        if (i==0 and j==5) or (i==1 and j==4) or (i==2 and j==3):
            continue
        m2_faces.append(dice[i]+dice[j])
m2 = min(m2_faces)

m3_faces = []
i, j, k = [0, 0, 0, 0, 1, 1, 2, 3], [1, 1, 2, 3, 2, 3, 4, 4], [2, 3, 4, 4, 5, 5, 5, 5]
for l in range(8):
    m3_faces.append(dice[i[l]]+dice[j[l]]+dice[k[l]])
m3 = min(m3_faces)

if n == 1:
    ans = d-max(dice)
else:
    ans = m1*(n-2)*4*(n-1) + m2*4*(n-1) + m3*4 + m1*(n-2)*(n-2) + m2*4*(n-2)
print(ans)