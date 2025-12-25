N, M = map(int, input().split())
arr = [input().strip() for _ in range(M)]
visited = [[0]*N for _ in range(M)]
B = 0
W = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:  # 방문기록 없으면 해당 지점부터 같은병사 있는곳으로 dfs
            cnt = 1  # 같은 나라 병사 수
            visited[i][j] = 1  # 방문기록
            stack = [(i, j)]
            while stack:
               si, sj = stack.pop()
               for di, dj in [[-1,0],[1,0],[0,1],[0,-1]]:
                   ni = si + di
                   nj = sj + dj
                   if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == 0:
                       if arr[ni][nj] == arr[i][j]:
                           visited[ni][nj] = 1
                           cnt = cnt + 1
                           stack.append((ni, nj))
            if arr[i][j] == 'B':  # 값 기록
                B = B + cnt ** 2
            else:
                W = W + cnt ** 2
print(W, B)