"""
문제 정의
1. 상자의 크기 M, N (NxM 배열)
2. 상자의 수 H
3. 인접한 곳에 있는 익지 않은 토마토는 익은 토마토의 영향을 받는다


로직 정의
1. 각 상자에 담긴 애들은 차등 없이 진행해야 한다
2. 3차원 배열로 푼다
-> 첫 인덱스가 높이
즉 arr[h][r][c] -> 층, 행, 열 순서로 정해진다
-> 문제 양식대로는 visited [H][N][M] 이런 형식

시작점은 토마토의 위치에서 부터 시작
토마토 1 -> bfs로 연결된 애들 이전 값 + 1 처리 (이후에 -1)
만약에 0 을 만나면 1로 바꾸기 (maps)
-1 을 만나면 cont


"""

from collections import deque
def check(h, i, j):
    if 0<= h < H and 0 <= i < N and 0 <= j < M:
        return True
    else:
        return False


def bfs(q):
    global mot
    dh = [0, 0, 0, 0, 1, -1]
    di = [1, 0, -1, 0, 0, 0]
    dj = [0, 1, 0, -1, 0, 0]
    while q:
        h, i, j = q.popleft()
        for d in range(6):
            nh, ni, nj = h+dh[d], i+di[d], j+dj[d]
            # 범위 벗어나면
            if not check(nh,ni,nj):
                continue
            # 토마토가 안들어있으면
            if maps[nh][ni][nj] == -1:
                continue
            # 토마토가 1 이면:
            if maps[nh][ni][nj] == 1:
                continue
            # 키울 토마토면 
            # 방문횟수 + 1
            if visited[nh][ni][nj] == 0:
                visited[nh][ni][nj] = visited[h][i][j] + 1
                q.append([nh,ni,nj])
                mot -= 1
    return



M, N, H = map(int, input().split())
maps = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
tom = 0
mot = 0
q = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if maps[h][i][j] == 1:
                tom += 1
                q.append([h, i, j])
                visited[h][i][j] = 1
            elif maps[h][i][j] == 0:
                mot += 1
bfs(q)
cnt = 0
for table in visited:
    for row in table:
        cnt = max(cnt, max(row))
print(-1 if mot else cnt-1)
