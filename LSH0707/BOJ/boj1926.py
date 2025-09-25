import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
def pic(si, sj):  # (시작i좌표, 시작j좌표)
    global cnt  # 그림 갯수 (bfs 1번당 1개)
    global max_a  # 인접 색칠 된 부분 찾을 때 마다 +1
    q = deque()
    q.append((si, sj))
    arr[si][sj] = 0  # 방문기록
    a = 1  # 초기 그림 넓이
    while q:
        ci, cj= q.popleft()  # bfs
        for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 1:
                    a = a + 1  # 넓이 기록
                    arr[ni][nj] = 0  # 방문 기록
                    q.append((ni, nj))  # q에 append
    cnt = cnt + 1  # 그림 갯수 기록
    if a > max_a:  # 최대 넓이
        max_a = a
    return
cnt = 0
max_a = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            pic(i, j)
print(cnt)
print(max_a)