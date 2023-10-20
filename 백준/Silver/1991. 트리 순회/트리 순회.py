n = int(input())
tree1 = []  # 전위순회
tree2 = []  # 중위순회
tree3 = []  # 후위순회
for _ in range(n):
    parent, left, right = map(str, input().split())

    # 전위순회
    if parent not in tree1:  # 첫번째
        tree1.append(parent)
    if left != '.' and left not in tree1:    # 왼쪽 자식이 tree1 에 없을 때
        i = tree1.index(parent)
        tree1.insert(i+1, left)
    if right != '.' and right not in tree1:  # 오른쪽 자식이 tree1 에 없을 때
        i = tree1.index(parent)
        if left == '.': # 왼쪽X 오른쪽O
            tree1.insert(i+1, right)
        else:   # 왼쪽O 오른쪽 O
            tree1.insert(i+2, right)

    # 중위순회
    if parent not in tree2:  # 첫번째
        tree2.append(parent)
    if left != '.' and left not in tree2:  # 왼쪽 자식이 tree1 에 없을 때
        i = tree2.index(parent)
        tree2.insert(i, left)
    if right != '.' and right not in tree2:  # 오른쪽 자식이 tree1 에 없을 때
        i = tree2.index(parent)
        tree2.insert(i+1, right)

    # 후위순회
    if parent not in tree3:  # 첫번째
        tree3.append(parent)
    if left != '.' and left not in tree3:    # 왼쪽 자식이 tree1 에 없을 때
        i = tree3.index(parent)
        tree3.insert(i, left)
    if right != '.' and right not in tree3:  # 오른쪽 자식이 tree1 에 없을 때
        i = tree3.index(parent)
        tree3.insert(i, right)

for node in tree1:
    print(node, end='')
print()
for node in tree2:
    print(node, end='')
print()
for node in tree3:
    print(node, end='')