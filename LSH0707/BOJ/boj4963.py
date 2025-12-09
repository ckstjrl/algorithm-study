import sys
input = sys.stdin.readline
from collections import deque
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]  # 1땅 0바다
    cnt = 0
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):  # 배열 전체 순회
            if arr[i][j] == 1 and visited[i][j] == 0:
            # 방문 기록 없는 땅이면 bfs로 방문 기록, cnt+1
                cnt = cnt + 1
                visited[i][j] = 1
                q = deque([(i, j)])
                while q:
                    si, sj = q.popleft()
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            ni = si + di
                            nj = sj + dj
                            if 0 <= ni < h and 0 <= nj < w:
                                if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                                    visited[ni][nj] = 1
                                    q.append((ni, nj))
    print(cnt)
