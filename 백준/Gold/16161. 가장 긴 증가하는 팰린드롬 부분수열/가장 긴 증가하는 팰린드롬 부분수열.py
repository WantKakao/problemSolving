
def find_lis_length(seq):
    """Longest Increasing Subsequence (LIS) 길이를 찾기 위한 이분 탐색 활용"""
    lis = []
    for num in seq:
        pos = bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
    return len(lis)


def longest_increasing_palindrome_length(S):
    n = len(S)
    max_length = 0

    # 각 위치를 팰린드롬의 중심으로 생각하여 양쪽으로 확장
    for center in range(n):
        # 홀수 길이 팰린드롬
        l, r = center, center
        subseq = [1e10]
        while l >= 0 and r < n and S[l] == S[r] and subseq[-1] > S[l]:
            subseq.append(S[l])  # 또는 S[r]을 추가해도 동일
            max_length = max(max_length, 2*(len(subseq)-1)-1)
            l -= 1
            r += 1

        # 짝수 길이 팰린드롬
        l, r = center, center + 1
        subseq = [1e10]
        while l >= 0 and r < n and S[l] == S[r] and subseq[-1] > S[l]:
            subseq.append(S[l])
            max_length = max(max_length, 2*(len(subseq)-1))
            l -= 1
            r += 1

    return max_length


# 입력 받기
N = int(input())
S = list(map(int, input().split()))

# 결과 출력
print(longest_increasing_palindrome_length(S))
