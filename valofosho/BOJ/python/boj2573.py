"""
문제 정의
1. 빙산 이외의 부분은 바닷물로 0으로 처리
2. 바닷물에 닿은 개수만큼 1년마다 녹는다
3. 동서남북으로 붙어있으면 하나의 덩어리로 취급
4. 빙산이 두 덩어리 이상으로 분리되는 최초의 시간을 구해라!

로직 정의
1. bfs로 각 빙산의 인근을 먼저 탐색 후 시간별로 바꿔주기
    -> 바꿔야 할 값을 하나의 맵을 더 만들어서 담아두고 한 번에 바꿔주기(안그러면 연쇄작용 나옴)
2. 바꿔준 후 한 지점에서 부터 덩어리 탐색
1~2를 반복
3. 만약 두 덩어리 이상으로 분리되지 않으면 0출력
추가 정보: 어차피 테두리는 무조건 바다임
"""
import sys
from collections import deque

def check(i,j):
    if 0 <= i < N and 0<= j < M:
        return True
    else:
        return False

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if check(ni,nj) and not visited[ni][nj] and maps[ni][nj] != 0:
                visited[ni][nj] = True
                q.append((ni,nj))
    return

input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
year = 0 
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
while True:
    year += 1
    temp = [[0] * M for _ in range(N)]
    # 맨끝 행, 열은 바다라서 범위 조정
    for i in range(1, N-1):
        for j in range(1, M-1):
            if maps[i][j] == 0:
                continue
            else:
                # 빙산이면 4방향 탐색
                for d in range(4):
                    ni, nj = i+di[d], j+dj[d]
                    if check(ni,nj) and maps[ni][nj] == 0:
                        # 바로 녹이면 안되니까 담아두기
                        temp[i][j] += 1
    for i in range(1, N-1):
        for j in range(1, M-1):
            if temp[i][j] != 0:
                # 녹여주기
                maps[i][j] -= temp[i][j]
                if maps[i][j] < 0:
                    maps[i][j] = 0
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(1,N-1):
        for j in range(M-1):
            # bfs 내 visited 처리로 하나의 덩이리만 찾아짐
            if maps[i][j] != 0 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    if cnt >= 2:
        break
    if cnt == 0:
        year = 0
        break
print(year)