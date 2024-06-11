import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))

    if sum(nums) == 0:
        break

    nums.sort()
    if nums[0] + nums[1] <= nums[2]:
        print("Invalid")
    elif nums[0] == nums[2]:
        print("Equilateral")
    elif nums[0] == nums[1] or nums[1] == nums[2]:
        print("Isosceles")
    else:
        print("Scalene")