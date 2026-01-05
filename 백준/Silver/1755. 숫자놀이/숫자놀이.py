l = [8, 5, 4, 9, 1, 7, 6, 3, 2, 0]
m, n = map(int, input().split())
am, bm = divmod(m, 10)
an, bn = divmod(n, 10)
ans = [8, 88, 85, 84, 89, 81, 87, 86, 83, 82, 80,
        5, 58, 55, 54, 59, 51, 57, 56, 53, 52, 50,
        4, 48, 45, 44, 49, 41, 47, 46, 43, 42, 40,
        9, 98, 95, 94, 99, 91, 97, 96, 93, 92, 90,
        1, 18, 15, 14, 19, 11, 17, 16, 13, 12, 10,
        7, 78, 75, 74, 79, 71, 77, 76, 73, 72, 70,
        6, 68, 65, 64, 69, 61, 67, 66, 63, 62, 60,
        3, 38, 35, 34, 39, 31, 37, 36, 33, 32, 30,
        2, 28, 25, 24, 29, 21, 27, 26, 23, 22, 20]

cnt = 0
for x in ans:
    if m <= x <= n:
        print(x, end=' ')
        cnt += 1
    if cnt == 10:
        cnt = 0
        print()

# ans = []
# for a in l:
#     if am <= a <= an:
#         if am == a == an:
#             for b in l:
#                 if bm <= b <= bn:
#                     ans.append(a*10+b)
#         elif am == a:
#             for b in l:
#                 if bm <= b:
#                     ans.append(a*10+b)
#         elif an == a:
#             for b in l:
#                 if b <= bn:
#                     ans.append(a*10+b)
#         else:
#             for b in l:
#                 ans.append(a*10+b)