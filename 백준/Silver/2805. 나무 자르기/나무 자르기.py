import sys
input = sys.stdin.readline

n, total = map(int, input().split())
trees = [*map(int, input().split())]

l = len(trees)
m = max(trees)


def cut_the_tree():
    left = 0
    right = m
    ans = 0
    while left <= right:
        center = (left + right) // 2
        sum = 0
        for tree in trees:
            cutted = tree - center
            if cutted > 0:
                sum += cutted
        if sum >= total:
            ans = center
            left = center + 1
        else:
            right = center - 1
    return ans

print(cut_the_tree())