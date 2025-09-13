n = int(input())
tree = list(map(int, input().split()))
k = int(input())
k_set = [k]

tree[k] = -2
while k_set:
    temp = []
    for k in k_set:
        for i in range(n):
            if tree[i] == k:
                tree[i] = -2
                temp.append(i)
    k_set = temp

has_child = [False for _ in range(n)]
for i in range(n):
    if tree[i] == -2:
        has_child[i] = True
for i in range(n):
    t = tree[i]
    if t >= 0:
        has_child[t] = True
        
ans = has_child.count(False)
print(ans)