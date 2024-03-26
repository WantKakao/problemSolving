import copy
t = int(input())
for _ in range(t):
    n = int(input())
    nums = [*map(int, input())]
    mines = [*map(str, input())]
    confirm = [0 for _ in range(n)]
    for i in range(n):
        if mines[i] == '#':
            mines[i] = 0
        else:
            mines[i] = 1
            confirm[i] = 1


    def findmine(nums, mines, confirm):
        temp = []
        minesum = mines[0] + mines[1]
        if confirm[0] == 0:
            temp.append(0)
        if confirm[1] == 0:
            temp.append(1)
        if nums[0] == minesum:
            confirm[0] = confirm[1] = 1
        elif nums[0] == minesum + len(temp):
            for t in temp:
                mines[t] = 1
            confirm[0] = confirm[1] = 1

        for i in range(1, n-1):
            temp = []
            minesum = mines[i-1] + mines[i] + mines[i+1]
            if confirm[i-1] == 0:
                temp.append(-1)
            if confirm[i] == 0:
                temp.append(0)
            if confirm[i+1] == 0:
                temp.append(1)
            if nums[i] == minesum:
                confirm[i-1] = confirm[i] = confirm[i+1] = 1
            elif nums[i] == minesum + len(temp):
                for t in temp:
                    mines[i+t] = 1
                confirm[i-1] = confirm[i] = confirm[i+1] = 1

        temp = []
        minesum = mines[n-2] + mines[n-1]
        if confirm[n-2] == 0:
            temp.append(n-2)
        if confirm[n-1] == 0:
            temp.append(n-1)
        if nums[n-1] == minesum:
            confirm[n-2] = confirm[n-1] = 1
        elif nums[n-1] == minesum + len(temp):
            for t in temp:
                mines[t] = 1
            confirm[n-2] = confirm[n-1] = 1


    for _ in range(100):
        findmine(nums, mines, confirm)
    if sum(confirm) == n:
        print(sum(mines))
    else:
        flag = 0
        nums1 = copy.deepcopy(nums)
        mines1 = copy.deepcopy(mines)
        confirm1 = copy.deepcopy(confirm)
        confirm1[0] = 1
        for _ in range(100):
            findmine(nums1, mines1, confirm1)
        for i in range(1, n-1):
            if nums1[i] != (mines1[i-1] + mines1[i] + mines1[i+1]):
                flag = 1
                break
        if nums1[0] != (mines1[0] + mines1[1]) or nums1[n-1] != (mines1[n-2] + mines1[n-1]):
            flag = 1
        if not flag:
            print(sum(mines1))
        else:
            nums1 = copy.deepcopy(nums)
            mines1 = copy.deepcopy(mines)
            confirm1 = copy.deepcopy(confirm)
            confirm1[0] = 1
            mines1[0] = 1
            for _ in range(100):
                findmine(nums1, mines1, confirm1)
            print(sum(mines1))
