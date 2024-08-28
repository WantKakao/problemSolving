from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))

lis = []  # LIS를 저장할 리스트

for num in nums:
    # lis에서 num이 들어갈 위치를 찾는다.
    pos = bisect_left(lis, num)
    
    # 만약 num이 lis의 끝보다 크다면 lis에 추가
    if pos == len(lis):
        lis.append(num)
    # 그렇지 않으면, 해당 위치의 값을 num으로 바꾼다.
    else:
        lis[pos] = num

# lis의 길이가 최장 증가 부분 수열의 길이
print(len(lis))
