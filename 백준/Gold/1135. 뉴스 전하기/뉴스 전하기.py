n = int(input())
parents = list(map(int, input().split()))
children = [[] for _ in range(n)]
for i in range(1, n):
    children[parents[i]].append(i)
    
def dfs(u):
    times = [dfs(v) for v in children[u]]
    if not times:  # 부하 없음
        return 0
    times.sort(reverse=True)
    max_time = 0
    for i, t in enumerate(times):
        max_time = max(max_time, t + i + 1)
    return max_time

print(dfs(0))