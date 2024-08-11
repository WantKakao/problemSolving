def is_good_sequence(sequence):
    length = len(sequence)
    # 부분 수열의 길이를 1부터 절반까지 확인
    for i in range(1, length // 2 + 1):
        # 마지막 i개의 수열이 그 앞 i개의 수열과 같은지 확인
        if sequence[-i:] == sequence[-2*i:-i]:
            return False
    return True

def find_good_sequence(sequence, N):
    # 수열의 길이가 N에 도달하면 출력하고 종료
    if len(sequence) == N:
        print(sequence)
        return True
    
    # 1, 2, 3을 차례대로 추가하며 좋은 수열을 찾는다.
    for num in '123':
        if is_good_sequence(sequence + num):
            if find_good_sequence(sequence + num, N):
                return True
    
    return False

def main():
    N = int(input().strip())
    find_good_sequence("", N)

if __name__ == "__main__":
    main()
