"""
1은 이동 가능 0 은 이동 불가
(1,1) - 1based index 에서 출발
(N,M)으로 이동할 때 지나야 하는 최소 칸 수 -> 최소 거리(BFS)
!!! 시작 위치와 도착 위치도 포함해서 센다!!!
입력은 각각 붙어서 입력으로 주어진다.
"""

from collections import deque
import sys

def check(i,j,N, M):
    if 0<=i<N and 0<=j<M:
        return True
    else:
        return False
def bfs(i,j, N, M):
    q = deque()
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    q.append([i,j])
    while q:
        i,j = q.popleft()
        for d in range(4):
            nx, ny = i+di[d], j+dj[d]
            if check(nx, ny, N, M):
                if visited[nx][ny] == 0 and maps[nx][ny] == 1: # 범위 내에 갈 수 있는 곳이면
                    visited[nx][ny] = visited[i][j] + 1 # 방문 처리
                    if nx == N-1 and ny == M-1: # 1-based 이므로 -1 연산
                        return visited
                    else:
                        q.append([nx,ny])
    return visited

input = sys.stdin.readline
N, M = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(N)]  # sys.stdin.readline 은 strip 필요
si, sj = 0, 0
visited = bfs(si,sj, N, M)
print(visited[N-1][M-1])    # 1-based 이므로 -1 연산