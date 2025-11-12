"""
BOJ1245. 농장 관리

[문제]
농부 민식이가 관리하는 농장은 N×M 격자로 이루어져 있다. 민식이는 농장을 관리하기 위해 산봉우리마다 경비원를 배치하려 한다. 이를 위해 농장에 산봉우리가 총 몇 개 있는지를 세는 것이 문제다.
산봉우리의 정의는 다음과 같다. 산봉우리는 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합으로 이루어져 있다.
여기서 "인접하다"의 정의는 X좌표 차이와 Y좌표 차이가 모두 1 이하인 경우이다. 또한 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야한다.
문제는 격자 내에 산봉우리의 개수가 총 몇 개인지 구하는 것이다.

[입력]
첫째 줄에 정수 N(1 < N ≤ 100), M(1 < M ≤ 70)이 주어진다.
둘째 줄부터 N+1번째 줄까지 각 줄마다 격자의 높이를 의미하는 M개의 정수가 입력된다. 격자의 높이는 500보다 작거나 같은 음이 아닌 정수이다.

[출력]
첫째 줄에 산봉우리의 개수를 출력한다.
"""

from collections import deque

import sys
input = lambda: sys.stdin.readline().rstrip()

# 인접 방향 델타 배열
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [1, 1, 0, -1, -1, -1, 0, 1]

# start 좌표에서 시작해 같은 높이를 가지는 연결 영역을 BFS로 탐색한 다음, 이 영역이 산봉우리인지 검사하는 함수
def check_hilltop(start):

    # BFS 준비
    q = deque([start])
    sy, sx = start
    checked[sy][sx] = True
    height = farm[sy][sx]   # height: 시작 칸의 높이
    hilltop = [(sy, sx)]    # 산봉우리 영역 후보에 시작 칸을 추가

    # BFS 시작
    while q:
        cur_y, cur_x = q.popleft()
        for dir in range(8):
            ny, nx = cur_y + dy[dir], cur_x + dx[dir]   # 인접 8칸을 다음 좌표로 설정
            # 다음 좌표가 농장 범위 내부이고, 검사를 아직 안했으며, 처음 높이와 같은 칸이면,
            if 0<=ny<N and 0<=nx<M and not checked[ny][nx] and farm[ny][nx] == height:
                q.append((ny, nx))  # 큐에 enqueue
                hilltop.append((ny, nx))    # 산봉우리 영역 후보에 추가
                checked[ny][nx] = True      # 검사 체크

    # BFS를 통과한 같은 높이의 연결 영역에 대하여 산봉우리인지 검사
    for each in hilltop:    # 연결 영역의 각각의 격자 칸을 순회하면서,
        ey, ex = each
        for dir in range(8):         # 인접 8칸을 다음 좌표로 설정
            ny, nx = ey + dy[dir], ex + dx[dir]
            if 0<=ny<N and 0<=nx<M:  # 다음 좌표가 범위 내부일 때, 다음을 검사함:
                if farm[ny][nx] > height:   # 다음 좌표가 현재 높이보다 크다면
                    return False            # 산봉우리가 아니므로 False 반환
                
    return True # 검사를 모두 통과했다면, 산봉우리이므로 True 반환


# main
N, M = map(int, input().split())            # N, M: 농장의 세로/가로 크기
farm = [list(map(int, input().split())) for _ in range(N)]  # 농장의 높이 정보
checked = [[False] * M for _ in range(N)]   # 검사 체크용 2차원 배열
cnt = 0     # cnt: 산봉우리의 개수
# 농장 내부의 모든 격자 칸을 순회하면서,
for y in range(N):
    for x in range(M):
        # 검사를 안했다면 산봉우리 검사 진행
        if not checked[y][x]:
            # 산봉우리이면, 카운트 증가
            if check_hilltop((y, x)):
                cnt += 1
                
print(cnt)  # 산봉우리 개수 출력