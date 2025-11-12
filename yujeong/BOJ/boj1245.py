# 1245. 농장 관리

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())    # 농장 크기 세로 N, 가로 M
grid = [list(map(int, input().split())) for _ in range(N)]  # 농장
visited = [[False] * M for _ in range(N)]       
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
        (1, -1), (-1, 1), (1, 1), (-1, -1)]     # 인접 방향들
mountain_cnt = 0    # 산봉우리 개수

# bfs로 인접한 격자들을 탐색하며 산봉우리 여부를 체크하기
def search(x, y):
    flag = True     # 산봉우리인지
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for dx, dy in dirs:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<M:             # 농장 범위 내에서 인접한 칸이
                if grid[nx][ny] > grid[cx][cy]: # 현재 높이보다 높으면 -> 산봉우리 아님
                    flag = False
                if grid[nx][ny] == grid[cx][cy] and not visited[nx][ny]:    # 같은 높이임 -> 탐색 계속
                    q.append((nx, ny))
                    visited[nx][ny] = True  # visited 체크
    return flag  # 산봉우리 여부 반환

# 농장 범위 내에서 각 칸 탐색하며 산봉우리 개수 세기
for i in range(N):
    for j in range(M):
        if not visited[i][j] and search(i, j):  # 방문한 적 없고 산봉우리인 칸이면
            mountain_cnt += 1                   # 개수 +1

print(mountain_cnt)
