"""
BOJ16234. 인구 이동

[문제]
N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.
오늘부터 인구 이동이 시작되는 날이다.
인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)
인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

[출력]
인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.
"""
from collections import deque

import sys
input = lambda: sys.stdin.readline().rstrip()

# 상하좌우 델타 배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 시작 위치(start)에서 BFS를 이용해 연합을 형성하는 함수
def form_union(start, L, R):

    # BFS 준비
    sy, sx = start
    q = deque([start])
    visited[sy][sx] = True
    union = [start]         # 연합에 속한 나라들의 좌표 리스트 union에 시작 국가의 좌표 start 넣기
    sum_union = A[sy][sx]   # 연합 전체 인구의 합 sum_union에 시작 국가의 인구 수 A[sy][sx] 누적하기

    # BFS
    while q:
        cur_y, cur_x = q.popleft()
        for dir in range(4):
            ny, nx = cur_y + dy[dir], cur_x + dx[dir]
            # 다음 국가가 격자 범위 내에 있고 아직 방문하지 않았으며, 인구 차이가 L 이상 R 이하라면 연합에 포함
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and L <= abs(A[ny][nx] - A[cur_y][cur_x]) <= R:
                q.append((ny, nx))
                union.append((ny, nx))  # union에 연합에 포함된 다음 국가 추가
                visited[ny][nx] = True
                sum_union += A[ny][nx]  # union에 연합에 포함된 다음 국가의 인구 수 누적
    
    return union, sum_union # 연합에 포함된 국가 좌표 목록 union과 인구 총합 sum_union을 반환

# main
N, L, R = map(int, input().split()) # N: 땅 크기, L: 최소 인구 차이, R: 최대 인구 차이
A = [list(map(int, input().split())) for _ in range(N)] # A: 각 나라의 인구 수 정보

# 인구 이동 시뮬레이션
day = 0 # 인구 이동이 발생한 총 일수

while True:
    moved = False   # 하루 동안 인구 이동이 있었는지 여부를 의미하는 moved를 False로 초기화
    visited = [[False] * N for _ in range(N)]   # BFS 방문 정보 초기화
    
    # 모든 나라를 순회하면서, 아직 방문하지 않은 나라를 기준으로 연합을 탐색
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                # 현재 나라를 시작점으로 연합 형성
                union, total = form_union((y, x), L, R)
                # 연합의 크기가 2 이상이면 국경이 열린 것이므로
                if len(union) > 1:
                    moved = True    # 인구 이동이 일어남
                    new_pop = total // len(union)   # 연합 내 새로운 평균 인구수 계산
                    # 연합 내 모든 나라의 인구를 새로운 평균값으로 갱신
                    for cy, cx in union:
                        A[cy][cx] = new_pop

    # 하루 동안 인구 이동이 없었다면, 시뮬레이션 종료
    if not moved:
        break

    # 하루가 지나면 일수 증가
    day += 1

# 인구 이동이 발생한 총 일수 출력
print(day)