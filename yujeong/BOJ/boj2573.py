# 2573. 빙산
import sys
input = sys.stdin.readline
from collections import deque

# 한 덩어리의 빙산을 탐색하며 녹아야 하는 얼음의 위치와 양을 기록해 반환하기
def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    melt_lst = []       # 녹일 빙산의 위치와 인접 바다 개수 저장할 리스트

    while q:
        cx, cy = q.popleft()
        sea_cnt = 0     # 인접 바다 개수 
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<M: # arr[cx][cy]에서 인접한 arr[nx][ny]가
                if not arr[nx][ny]: # 바다
                    sea_cnt += 1    # 인접 바다 개수 +1
                elif arr[nx][ny] and not visited[nx][ny]:   # 빙산
                    q.append((nx, ny))                      # 다음에 탐색
                    visited[nx][ny] = True
        if sea_cnt:     # arr[cx][cy]가 바다에 인접한 얼음이면
            melt_lst.append((cx, cy, sea_cnt))  # (cx, cy, 녹일 칸 수) 저장

    return melt_lst     # 덩어리 다 탐색 완료; 녹여야 하는 위치와 양 담은 리스트 반환

# 바다에 인접한 만큼 녹아야 하는 빙산을 녹이기 
def melt_ice(melt_list):
    for x, y, sea_cnt in melt_list:
        arr[x][y] = max(0, arr[x][y] - sea_cnt)     # 녹이기 (0보다 작아질 수는 없음)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ice_lst = [(i, j) for i in range(N) for j in range(M) if arr[i][j] > 0]     # 얼음이 있는 위치들
year = 0    # 경과한 햇수

while True:
    cnt = 0     # 이번 해에 있는 빙산 덩어리 수
    visited = [[False]*M for _ in range(N)]
    full_melt_list = []     # 이번 해가 지나며 녹일 빙산들 위치와 칸 수

    # 빙산들을 방문하며 녹일 정보 기록
    for i, j in ice_lst:
        if not visited[i][j] and arr[i][j]:
            full_melt_list += bfs(i, j)
            cnt += 1    # bfs로 탐색 완료 = 한 덩어리 

    if cnt >= 2:    # 빙산이 두 덩어리 이상으로 분리됨
        print(year) # 지금까지 걸린 시간(년) 출력하고 break
        break

    if cnt == 0:    # 분리된 적이 없는데 얼음 없음 (다 녹음)
        print(0)    # 0 출력하고 break
        break

    melt_ice(full_melt_list)    # 종료되지 않음; 빙산 녹이기
    ice_lst = [(i, j) for i, j in ice_lst if arr[i][j] > 0] # 얼음 위치 리스트 갱신

    year += 1   # 시간 +1
