# 14466. 소가 길을 건너간 이유 6

from collections import deque
import sys
input = sys.stdin.readline

N, K, R = map(int, input().split())     # 격자 N*N, 소 K마리, 길 R개

# 길 정보
roads = [[[] for _ in range(N+1)] for _ in range(N+1)]
for _ in range(R): 
    r1, c1, r2, c2 = map(int, input().split())
    roads[r1][c1].append((r2, c2))
    roads[r2][c2].append((r1, c1))

# 소 정보
cows = []
for _ in range(K): 
    r, c = map(int, input().split())
    cows.append((r, c))

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# BFS로 각 소에서 길을 건너지 않고 다른 소들에 가는 방법 탐색
def bfs(cow_n, r, c):
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    q = deque([(r, c)])
    visited[r][c] = True
    while q:
        px, py = q.popleft()
        for dx, dy in dirs:
            nx, ny = px+dx, py+dy
            # 상하좌우 이동 시 농장 범위 내에 있고, 방문한 적 없고, 길을 안 건너고 갈 수 있으면 이동
            if 0<nx<=N and 0<ny<=N and not visited[nx][ny] and (nx, ny) not in roads[px][py]:
                q.append((nx, ny))
                visited[nx][ny] = True
    
    # 이 소가 길을 건너지 않고 이동하지 못한 소 개수 리턴
    # 쌍을 셀 때 중복 방지를 위해 지금 소 번호보다 이후 번호에 대해서만 카운트 
    return sum(not visited[x][y] for x, y in cows[cow_n:])

cnt = 0     # 길 건너지 않고 만날 수 없는 소 쌍 개수 
for i in range(K):
    cow_r, cow_c = cows[i]
    cnt += bfs(i, cow_r, cow_c)
print(cnt)
