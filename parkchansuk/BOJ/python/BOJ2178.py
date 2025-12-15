# BOJ 2178. 미로 탐색 / D3
'''
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때,
(1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
'''
import sys
from collections import deque

def find_route(maze, N, M):
    visit_arr = [[0]*M for _ in range(N)]
    q = deque([])
    q.append([0, 0])
    visit_arr[0][0] = 1
    while q:
        ti, tj = q.popleft()
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni = ti + di
            nj = tj + dj
            if 0<= ni < N and 0 <= nj < M and maze[ni][nj] != 0 and visit_arr[ni][nj] == 0:
                q.append([ni, nj])
                visit_arr[ni][nj] = visit_arr[ti][tj] + 1
                if ni == N-1 and nj == M-1:
                    return visit_arr[ni][nj]

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
ans = find_route(maze, N, M)
print(ans)