import sys
sys.setrecursionlimit(10000)
R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(R)]
visited_alpha = set()
max_len = 0

def dfs(pi, pj, count):
    global max_len
    max_len = max(max_len, count)

    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        ni, nj = pi + di, pj + dj
        if 0 <= ni < R and 0 <= nj < C:
            if arr[ni][nj] not in visited_alpha:
                visited_alpha.add(arr[ni][nj])
                dfs(ni, nj, count + 1)
                visited_alpha.remove(arr[ni][nj])

visited_alpha.add(arr[0][0])
dfs(0, 0, 1)
print(max_len)