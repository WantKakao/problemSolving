# 2485 가로수
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# trees = []
# for _ in range(n):
#     trees.append(int(input()))
#
#
# def GCD(x, y):
#     if x >= y:
#         if x % y == 0:
#             return y
#         else:
#             return GCD(x % y, y)
#     else:
#         if y % x == 0:
#             return x
#         else:
#             return GCD(x, y % x)
#
#
# n1 = trees[1] - trees[0]
# for i in range(2, n):
#     n2 = trees[i] - trees[i-1]
#     temp = GCD(n1, n2)
#     n1 = temp
#
# denominator = trees[n-1] - trees[0]
# nominator = n1
# print(denominator // nominator + 1 - n)


# 2529 부등호
from itertools import permutations

n = int(input())
op = list(map(str, input().split()))

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
rev_nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

mini = permutations(nums, n+1)
maxi = permutations(rev_nums, n+1)


def validation(array):
    for num_list in array:
        is_true = True

        for i in range(n):
            if op[i] == '<':
                if num_list[i] >= num_list[i+1]:
                    is_true = False
                    break
            else:
                if num_list[i] <= num_list[i+1]:
                    is_true = False
                    break
        if is_true:
            return [str(i) for i in num_list]


minimum = validation(mini)
maximum = validation(maxi)
print(''.join(maximum))
print(''.join(minimum))