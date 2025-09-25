"""
BOJ1261. 알고스팟

[문제]
알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다. 미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.
알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다. 어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 단, 미로의 밖으로 이동 할 수는 없다.
벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.
만약 이 문제가 알고스팟에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 안타깝게도 이 문제는 Baekjoon Online Judge에 수록되어 있기 때문에, sudo를 사용할 수 없다.
현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다. 0은 빈 방을 의미하고, 1은 벽을 의미한다.
(1, 1)과 (N, M)은 항상 뚫려있다.

[출력]
첫째 줄에 알고스팟 운영진이 (N, M)으로 이동하기 위해 벽을 최소 몇 개 부수어야 하는지 출력한다.
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

from heapq import heappop, heappush

# 상하좌우 방향 (델타 배열)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def min_walls_to_break(start, goal):    # start부터 goal까지 최소 벽을 몇 개 부수어야 하는지 구하는 함수

    sy, sx = start  # sy, sx = start의 y좌표, x좌표
    pq = [(0, sy, sx)]   # 우선순위 큐: (부순 벽 개수, y좌표, x좌표), 항상 지금까지 벽을 가장 적게 부순 경로부터 탐색
    min_breaks = [[INF] * M for _ in range(N)]  # min_breaks[y][x] = (y, x)에 도착하기까지 부순 벽의 최소 개수
    min_breaks[sy][sx] = 0  # 시작점은 부순 벽 개수 0으로 초기화

    while pq:
        # 현재까지 부순 벽 개수가 가장 적은 위치를 꺼냄
        cur_broken, cur_y, cur_x = heappop(pq)

        # 이미 더 적은 벽으로 방문한 적이 있다면 스킵
        if min_breaks[cur_y][cur_x] < cur_broken:
            continue

        # 4방향 이동 시도
        for dir in range(4):
            ny, nx = cur_y + dy[dir], cur_x + dx[dir]

            # 미로 범위 체크
            if 0 <= ny < N and 0 <= nx < M:
                # 벽(1)이면 벽을 하나 더 부숴야 함
                if maze[ny][nx] == '1':
                    new_broken = cur_broken + 1
                # 빈 방(0)이면 벽 개수 변화 없음
                else:
                    new_broken = cur_broken

                # 지금까지 구한 최소 벽 개수보다 더 많이 부쉈다면 의미 없음 → 스킵
                if min_breaks[ny][nx] <= new_broken:
                    continue

                # 더 적게 부순 경로 발견 → 갱신
                min_breaks[ny][nx] = new_broken
                # 우선순위 큐에 넣어서 탐색 계속
                heappush(pq, (new_broken, ny, nx))

    # 목표 지점까지 최소 벽 부순 개수 반환
    gy, gx = goal
    return min_breaks[gy][gx]


# main
INF = int(21e8)
M, N = map(int, input().split())  # M = 미로의 가로 크기, N = 미로의 세로 크기
maze = [list(input().strip()) for _ in range(N)]  # 미로 정보 입력 ('0' 또는 '1')

# (0,0) → (N-1,M-1) 까지 이동할 때 필요한 최소 벽 부수기 개수 출력
print(min_walls_to_break((0, 0), (N - 1, M - 1)))
