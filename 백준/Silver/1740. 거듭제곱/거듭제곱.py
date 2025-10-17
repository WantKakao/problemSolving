n = int(input())
def bin_to_pow3(n):
    result = 0
    i = 0
    while n > 0:
        if n & 1:  # 해당 비트가 1이면
            result += 3**i
        n >>= 1
        i += 1
    return result
print(bin_to_pow3(n))