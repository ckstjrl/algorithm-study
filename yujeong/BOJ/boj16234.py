# 16234. 인구 이동 

import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())     # 땅 N*N, 인구 차이 L<=x<=R이면 개방
grid = [list(map(int, input().split())) for _ in range(N)]  # 각 칸별 인구수
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]                   # 상하좌우 이동 방향

day_cnt = 0     # 인구 이동이 발생한 일수 

# 주어진 칸에서 인접 칸을 bfs로 탐색하며 연합할 칸을 모두 찾기 
def bfs(x, y):
    q = deque([(x, y)])
    country_cnt = 1             # 연합을 이루는 칸 개수 
    population = grid[x][y]     # 연합 인구수
    visited[x][y] = True
    countries = [(x, y)]        # 연합 칸 좌표들 저장
    while q:
        cx, cy = q.popleft()
        for dx, dy in dirs:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:     # 인접하고, 방문한 적 없고
                if L <= abs(grid[nx][ny] - grid[cx][cy]) <= R:  # 인구수 차이가 L<=x<=R
                    country_cnt += 1
                    population += grid[nx][ny]
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    countries.append((nx, ny))
    # 연합을 이루는 칸 개수가 1보다 큼; 연합 필요
    if country_cnt > 1:
        union(countries, country_cnt, population)
        return True     # 인구 이동 발생함
    return False        # 인구 이동 발생 x

# 연합에 따라 인구 이동 진행하기
def union(lst, n, p):   # 연합을 이루는 칸들 좌표, 칸 개수, 인구수
    new_p = p // N      # 각 칸의 인구수
    for x, y in lst:
        grid[x][y] = new_p  # 연합을 이루는 칸들의 인구수 갱신

# 인구 이동이 발생하는 동안 while loop 내에서 일수 카운트 +1
while True:
    moved = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and bfs(i, j):
                moved = True
    # 인구 이동 발생하지 않으면 종료
    if not moved:
        break
    day_cnt += 1

print(day_cnt)