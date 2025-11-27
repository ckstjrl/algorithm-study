# 2638. 치즈

from collections import deque

N, M = map(int, input().split())    # 모눈종이 크기 세로 N, 가로 M
grid = [list(map(int, input().split())) for _ in range(N)]  # 모눈종이에 치즈 표시
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]   # 탐색할 때 움직일 방향 (상하좌우 인접)

# bfs로 모눈종이의 외부 공기 영역을 탐색하며 치즈를 녹이고, 치즈 녹였는지 여부를 반환
def melt_cheese():
    visited = [[0] * M for _ in range(N)]
    q = deque([(0, 0)])     # 좌상단 가장자리에서부터 시작
    visited[0][0] = 1
    melted = False          # 이번 턴에 치즈 녹였는지 여부 기록
    while q:
        px, py = q.popleft()
        for dx, dy in dirs:
            nx, ny = px+dx, py+dy
            if 0<=nx<N and 0<=ny<M:     # 모눈종이 범위 내에서
                if grid[nx][ny] == 0 and visited[nx][ny] == 0:  # 외부 공기인 경우
                    q.append((nx, ny))  # 다음에 탐색하기 위해 큐에 넣고
                    visited[nx][ny] = 1 # 방문 기록
                elif grid[nx][ny] == 1:     # 치즈인 경우
                    visited[nx][ny] += 1    # 외부 공기에 닿은 횟수 +1
    
    # 치즈가 외부 공기에 두 면 이상 접촉되었으면 녹이기
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and visited[i][j] >= 2:  
                grid[i][j] = 0
                melted = True   # 녹였다고 기록 

    return melted

time = 0    # 시간 기록
while True:
    if not melt_cheese():   # 이번 턴에 녹은 치즈 없으면 더 이상 치즈 없음
        break        
    time += 1   # 그 외; 시간 +1, 한 시간 후 녹일 치즈 탐색

print(time)
