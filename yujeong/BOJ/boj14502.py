# 14502. 연구소
from collections import deque
import sys
input = sys.stdin.readline

# 제한 N, M의 크기가 작다 ... 가능한 경우를 전부 탐색해서 최대 안전영역 구하기
# 백트래킹으로

N, M = map(int, input().split())    # 연구소 크기 세로 N, 가로 M
area = [list(map(int, input().split())) for _ in range(N)]  # 연구소 정보
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
virus_coords = []   # 바이러스가 있는 위치들 미리 저장 
for i in range(N):
    for j in range(M):
        if area[i][j] == 2:
            virus_coords.append((i, j))

res = 0

# bfs로 탐색하며 바이러스 전파하고 안전영역 개수 찾기
def search():
    q = deque(virus_coords) # 바이러스가 있는 위지 저장
    # 현재 상태(벽 세운 경우) 에서의 바이러스 전파 모습을 보기 위해
    # 원본 연구소 배열을 건드리지 x, 복사해서 탐색
    curr_area = [row[:] for row in area]    
    while q:
        cx, cy = q.popleft()
        for dx, dy in dirs:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<M:
                if curr_area[nx][ny] == 0:
                    curr_area[nx][ny] = 2   # 바이러스 전파 
                    q.append((nx, ny))

    # 안전 영역 개수 세기
    global res
    safe_cnt = 0
    for x in range(N):
        for y in range(M):
            if curr_area[x][y] == 0:
                safe_cnt += 1

    res = max(res, safe_cnt)    # 안전 영역 개수 갱신


# 백트래킹으로 가능한 곳에 벽 세우고 3개 세웠으면 바이러스 전파
def backtracking(cnt):
    if cnt == 3:    # 벽 3개 다 세움; 바이러스 전파해보기
        search()
        return
    for x in range(N):
        for y in range(M):
            if area[x][y] == 0:
                area[x][y] = 1          # 벽 세우고
                backtracking(cnt + 1)   # 다음 벽
                area[x][y] = 0          # 벽 없애고

backtracking(0)     # 벽 0개에서 탐색 시작

print(res)
