# 7569. 토마토
import sys
input = sys.stdin.readline
from collections import deque

# bfs로 3차원 배열 box를 탐색하며 익은 토마토에 인접한 토마토를 차례로 변화시키기 위한 함수 bfs()
def bfs():
    while q:
        px, py, pz = q.popleft()
        # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
        for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0)]:
            nx, ny, nz = px+dx, py+dy, pz+dz
            if 0<=nx<H and 0<=ny<N and 0<=nz<M and box[nx][ny][nz] == 0:
                # 익은 날짜 하루씩 +
                box[nx][ny][nz] = box[px][py][pz] + 1
                q.append((nx, ny, nz))

# 최종 결과 날짜수를 출력하기 위한 함수 check_tomato()
def check_tomato(arr):
    day = 0
    for floor in arr:
        for row in floor:
            for col in row:
                if col == 0:
                    return -1   # 하나라도 안 익은 토마토가 있으면 -1 리턴
            day = max(day, max(row))
    return day - 1  # 시작을 1일로 했기 때문에 -1 

M, N, H = map(int, input().split())     # 가로 M, 세로 N, 높이 H

box = [[]*N for _ in range(H)]

# 3차원 배열 box에 토마토 담기
for i in range(H):
    for j in range(N):
        box[i].append(list(map(int, input().split())))

# 초기 상태가 익은 상태인 토마토들 위치 큐에 담기 
q = deque([])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append((i, j, k))

bfs()   # 토마토 익히기 
ans = check_tomato(box) # 익힌 결과에서 날짜 구하기
print(ans)