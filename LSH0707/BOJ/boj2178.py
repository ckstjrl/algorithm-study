from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
def dist():
    i, j = 0, 0
    visited[i][j] = 1  # 값 초기화
    q = deque()
    q.append([i, j])  # 큐에 값 추가
    while q:
        p = q.popleft()
        pi = p[0]
        pj = p[1]
        if pi == N-1 and pj == M-1:
            return visited[pi][pj]
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:  # 상하좌우 이동
            ni = pi + di
            nj = pj + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:  # 방문한적없고 길일경우
                q.append([ni, nj])  # 큐에 값 추가
                visited[ni][nj] = visited[pi][pj] + 1  # 이동거리 visited에 갱신
print(dist()) 