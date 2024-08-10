import sys

input = sys.stdin.readline

n = int(input())
trees = []
for _ in range(n):
    trees.append(int(input()))


def GCD(x, y):
    if x >= y:
        if x % y == 0:
            return y
        else:
            return GCD(x % y, y)
    else:
        if y % x == 0:
            return x
        else:
            return GCD(x, y % x)


n1 = trees[1] - trees[0]
for i in range(2, n):
    n2 = trees[i] - trees[i-1]
    temp = GCD(n1, n2)
    n1 = temp

denominator = trees[n-1] - trees[0]
nominator = n1
print(denominator // nominator + 1 - n)