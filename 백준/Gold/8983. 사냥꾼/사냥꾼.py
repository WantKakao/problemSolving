import sys
input = sys.stdin.readline

Point, Animals, Range = map(int, input().split())
ShootingPoints = [*map(int, input().split())]
AnimalLocations = []
for _ in range(Animals):
    AnimalLocations.append([*map(int, input().split())])
ShootingPoints.sort()


def distance_of_closest_point(x):
    left = 0
    right = Point - 1
    distance = 999999999
    while left < right+1:
        center = (left + right) // 2
        p = ShootingPoints[center]
        if x == p:
            return 0
        elif x < p:
            right = center - 1
        else:
            left = center + 1
    if left == Point:
        left -= 1
    if right == -1:
        right += 1
    return min((abs(x - ShootingPoints[left]), abs(ShootingPoints[right] - x)))


ans = 0
for x, y in AnimalLocations:
    if distance_of_closest_point(x) + y <= Range:
        ans += 1
print(ans)