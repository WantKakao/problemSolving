def solve(n):
    MOD = 100000  # 마지막 5자리
    
    ans = 1
    cnt2 = 0
    cnt5 = 0
    
    for i in range(2, n+1):
        x = i
        
        # 2 제거
        while x % 2 == 0:
            x //= 2
            cnt2 += 1
        
        # 5 제거
        while x % 5 == 0:
            x //= 5
            cnt5 += 1
        
        ans = (ans * x) % MOD
    
    # 남은 2 처리
    for _ in range(cnt2 - cnt5):
        ans = (ans * 2) % MOD
    
    return str(ans).zfill(5)


n = int(input())
print(solve(n))
