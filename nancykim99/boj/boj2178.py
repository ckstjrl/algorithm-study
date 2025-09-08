from collections import deque

def bfs(i, j, N, M) : # 탐색 시작점 i, j, 그래프 N, M
    visited = [[0] * M for _ in range(N)]
    q = deque([[i, j]])
    visited[i][j] = 1 # 시작점
    while q:
        ti, tj = q.popleft()
        if ti == N-1 and tj == M-1:
            return visited[ti][tj]
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti + di, tj + dj
            if 0<=wi<N and 0<=wj<M and maze[wi][wj] == '1' and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

ans = bfs(0, 0, N, M)
if ans is None:
    ans = 0

print(ans)



