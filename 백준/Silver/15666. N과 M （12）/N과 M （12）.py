n, m = map(int, input().split())
arr = list(map(int, input().split()))

temp = set(arr)
nums = list(temp)
nums.sort()
l = len(nums)
seq = []


def print_sequence(start, seq):
    for i in range(start, l):
        seq.append(nums[i])
        if len(seq) == m:
            for s in seq:
                print(s, end=' ')
            print()
        else:
            print_sequence(i, seq)
        seq.pop()


print_sequence(0, seq)