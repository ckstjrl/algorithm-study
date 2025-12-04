"""
BOJ4963. 섬의 개수

[문제]
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 
두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

[입력]
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
입력의 마지막 줄에는 0이 두 개 주어진다.

[출력]
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
"""

from collections import deque

import sys
input = lambda: sys.stdin.readline().rstrip()

# 8방향 델타 배열(→, ↗, ↑, ↖, ←, ↙, ↓, ↘)
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [1, 1, 0, -1, -1, -1, 0, 1]

# bfs로 섬을 찾는 함수 (연결 영역을 모두 체크)
def check_island(start):

    # BFS 준비
    sy, sx = start
    q = deque([start])
    checked[sy][sx] = True  # 시작점 방문 체크

    # BFS
    while q:
        cur_y, cur_x = q.popleft()
        for dir in range(8):    # 인접한 가로/세로/대각선 8방향을 순회하면서,
            ny, nx = cur_y + dy[dir], cur_x + dx[dir]   # 해당 방향으로의 1칸을 다음 좌표로 설정
            # 만약 다음 좌표가 지도 범위 내부에 있고, 땅(1)이며, 검사하지 않았다면:
            if 0<=ny<h and 0<=nx<w and sea_map[ny][nx] == 1 and not checked[ny][nx]:
                q.append((ny, nx))  # 큐에 추가
                checked[ny][nx] = True  # 검사 체크

# main
while True:

    # w: 너비(가로), h: 높이(세로)
    w, h = map(int, input().split())

    # 입력 마지막 줄(0 0)이면 종료
    if w == 0 and h == 0:
        break

    # 입력 마지막 줄이 아닌 경우,
    else:
        sea_map = [list(map(int, input().split())) for _ in range(h)]   # 지도 정보
        checked = [[False] * w for _ in range(h)]   # 검사(방문) 여부 체크 배열
        cnt = 0 # 섬 개수 카운트하는 변수

        # 모든 칸을 순회하면서,
        for y in range(h):
            for x in range(w):
                # 방문하지 않은 땅 발견 시 BFS 실행하여 그 땅과 연결된 모든 칸을 검사 체크
                if sea_map[y][x] == 1 and not checked[y][x]:
                    check_island((y, x))    # BFS로 연결된 모든 땅 방문 처리
                    cnt += 1    # 섬 개수 count

        # 해당 테스트 케이스의 섬 개수 출력
        print(cnt)