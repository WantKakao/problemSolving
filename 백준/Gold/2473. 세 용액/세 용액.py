def find_closest_to_zero_solution(N, properties):
    properties.sort()
    closest_sum = float('inf')
    result = []

    for i in range(N - 2):
        left = i + 1
        right = N - 1

        while left < right:
            current_sum = properties[i] + properties[left] + properties[right]

            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
                result = [properties[i], properties[left], properties[right]]

            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                # If the current_sum is 0, this is the closest we can get
                return properties[i], properties[left], properties[right]

    return result


# 입력을 처리하는 부분
N = int(input())
properties = list(map(int, input().split()))

# 가장 가까운 용액을 찾고 출력
result = find_closest_to_zero_solution(N, properties)
print(result[0], result[1], result[2])
