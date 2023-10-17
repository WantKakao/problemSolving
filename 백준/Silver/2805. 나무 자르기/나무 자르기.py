N, M = map(int, input().split())
arr = [*map(int, input().split())]
s, e = 0, max(arr)
ans = 0

while s <= e:
    res = 0
    m = (s + e) // 2

    for tree in arr:
        if tree > m:
            res += tree - m
    
    if res >= M: 
        s = m + 1
        ans = m  # 조건을 만족하는 이 때만 답을 저장해야 함
    else:
        e = m - 1  # 여기는 m을 무조건 줄여야 함. 여기서 답을 찾는 게 아님. if문에서 알아서 찾아짐

print(ans)