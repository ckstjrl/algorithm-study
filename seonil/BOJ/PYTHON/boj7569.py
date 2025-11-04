"""
BOJ7569. 토마토
[문제]
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다.
창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.
토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

[입력]
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.
토마토가 하나 이상 있는 경우만 입력으로 주어진다.

[출력]
여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
"""

import sys
input = sys.stdin.readline

from collections import deque

# 델타 : 상하좌우앞뒤 방향
dz = [0, 0, 0, 0, -1, 1]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]

def min_days_to_ripen(tomatoes_info, M, N, H):  # 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산하는 함수

    # BFS 준비
    visited = [[[-1] * M for _ in range(N)] for _ in range(H)] # visited : 방문 정보 기록, default 방문 체크 '-1'
    q = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                # 격자 상자 내부의 익은 토마토들은 전부 큐에 넣고 방문 체크 '0'(0일차)
                if tomatoes_info[i][j][k] == 1:
                    q.append((i, j, k))
                    visited[i][j][k] = 0
                # 격자 상자 내부의 토마토가 들어있지 않는 칸들은 방문 체크 '-2'(아예 사용 안할거임)
                elif tomatoes_info[i][j][k] == -1:
                    visited[i][j][k] = -2

    # visited : 익은 토마토 '0', 익지 않은 토마토 '-1', 토마토 없는 칸 '-2'인 상태로 BFS 시작

    # BFS
    while q: # 큐가 비어 있을 때까지 다음을 반복한다.

        rz, ry, rx = q.popleft()    # 큐에서 익은 토마토의 좌표를 꺼낸다

        for dir in range(6):    # 상하좌우앞뒤 6방향을 순회하면서:
            nz, ny, nx = rz + dz[dir], ry + dy[dir], rx + dx[dir]   # 다음 좌표는 각 방향으로 1칸 이동한 좌표
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and visited[nz][ny][nx] == -1:   # 다음 좌표가 범위 내부이고, 방문하지 않은 익지 않은 토마토 칸이면
                q.append((nz, ny, nx))  # 다음 좌표를 큐에 넣고
                visited[nz][ny][nx] = visited[rz][ry][rx] + 1   # 다음 visited 좌표에 현재 방문 날짜 수 + 1을 기록

    # visited(방문 날짜) 검사해서 다 탐색하는 데 걸린 최대 시간 찾기
    max_v = 0
    is_all_ripened = True   # default: 모든 토마토가 익었다고 가정함
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if visited[i][j][k] == -1:  # 만약 visited에서 한번이라도 -1이 발견되었다면, 토마토가 모두 익지는 못하는 상황이므로 체크
                    is_all_ripened = False
                elif visited[i][j][k] > max_v:    # visited의 최댓값을 갱신하면서, 인접한 토마토들이 전부 익는 데 걸린 최대 시간 저장
                    max_v = visited[i][j][k]
    return max_v if is_all_ripened else -1  # 토마토가 모두 익었다면 인접한 토마토들이 전부 익는 데 걸린 최대 시간을, 아니라면 -1을 반환

# main
M, N, H = map(int, input().split()) # M : 가로, N : 세로, H: 높이
tomatoes_info = []  # 토마토 농장의 격자모양 상자 정보
for _ in range(H): # H번 동안,
    layer = [list(map(int, input().split())) for _ in range(N)] # 각 층의 정보를 입력받고
    tomatoes_info.append(layer) # 쌓아 올린다.

min_days = min_days_to_ripen(tomatoes_info, M, N, H) # BFS를 이용하여 토마토가 모두 익을 때까지 최소 며칠이 걸리는지 계산
print(min_days) # 계산 결과 반환
