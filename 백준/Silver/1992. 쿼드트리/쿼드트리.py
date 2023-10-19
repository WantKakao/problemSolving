import sys
input = sys.stdin.readline

n = int(input())
tree = []
for _ in range(n):
    tree.append(list(input().rstrip()))

# print(tree)
ans = ''

def quad(i, j, n):
    global ans
    sum = 0
    for x in range(i, i+n):
        for y in range(j, j+n):
           sum += int(tree[x][y])

    if sum == n**2:  # 전부 1 인 경우
       ans += '1'
    elif sum == 0:  # 전부 0 인 경우
        ans += '0'
    else:
        ans += '('
        quad(i, j, n//2)
        quad(i, j+n//2, n//2)
        quad(i+n//2, j, n//2)
        quad(i+n//2, j+n//2, n//2)
        ans += ')'

quad(0, 0, n)
print(ans)