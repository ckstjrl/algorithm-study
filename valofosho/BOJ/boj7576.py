def check(i, j):
    if 0 <= i < N and 0 <= j < M:
        return True
    else:
        return False
    
def bfs(q):
    global mot
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    while q:
        i, j = q.popleft()
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if not check(ni,nj):
                continue
            if visited[ni][nj] != 0:
                continue
            if maps[ni][nj] != 0:
                continue
            visited[ni][nj] = visited[i][j] + 1
            q.append([ni,nj])
            mot -= 1
    return

from collections import deque
M, N = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
q = deque()
tomato = 0
mot = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            q.append([i,j])
            visited[i][j] = 1
        elif maps[i][j] == 0:
            mot += 1
bfs(q)
cnt = 0
for row in visited:
    cnt = max(cnt, max(row))


print(-1 if mot else cnt-1)
