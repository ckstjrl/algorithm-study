"""
BOJ2468. 안전 영역

[문제]
재난방재청에서는 많은 비가 내리는 장마철에 대비해서 다음과 같은 일을 계획하고 있다.
먼저 어떤 지역의 높이 정보를 파악한다. 그 다음에 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사하려고 한다.
이때, 문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.
어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수이다.
예를 들어, 다음은 N=5인 지역의 높이 정보이다.

6	8	2	6	2
3	2	3	4	6
6	7	3	3	2
7	2	5	3	6
8	9	5	2	7

이제 위와 같은 지역에 많은 비가 내려서 높이가 4 이하인 모든 지점이 물에 잠겼다고 하자. 이 경우에 물에 잠기는 지점을 회색으로 표시하면 다음과 같다.

6	8	2	6	2
3	2	3	4	6
6	7	3	3	2
7	2	5	3	6
8	9	5	2	7

물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역을 말한다.
위의 경우에서 물에 잠기지 않는 안전한 영역은 5개가 된다(꼭짓점으로만 붙어 있는 두 지점은 인접하지 않는다고 취급한다).

또한 위와 같은 지역에서 높이가 6이하인 지점을 모두 잠기게 만드는 많은 비가 내리면 물에 잠기지 않는 안전한 영역은 아래 그림에서와 같이 네 개가 됨을 확인할 수 있다.

6	8	2	6	2
3	2	3	4	6
6	7	3	3	2
7	2	5	3	6
8	9	5	2	7

이와 같이 장마철에 내리는 비의 양에 따라서 물에 잠기지 않는 안전한 영역의 개수는 다르게 된다.
위의 예와 같은 지역에서 내리는 비의 양에 따른 모든 경우를 다 조사해 보면 물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5임을 알 수 있다.
어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오.

[입력]
첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. N은 2 이상 100 이하의 정수이다. 둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 높이는 1이상 100 이하의 정수이다.

[출력]
첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.
"""

from collections import deque

import sys
input = lambda: sys.stdin.readline().rstrip()

# 상하좌우 델타 배열
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 안전 지역의 시작 지점부터 인접한 최대 크기의 안전 지역을 검사하는 함수
def check_safe(start, rain_level):

    # BFS 준비
    sy, sx = start
    q = deque([start])
    visited[sy][sx] = True

    # BFS 시작
    while q:
        cur_y, cur_x = q.popleft()
        for dir in range(4):
            ny, nx = cur_y + dy[dir], cur_x + dx[dir]   # 현재 지점과 상하좌우로 인접한 지점을 다음 지점으로 설정
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and heights[ny][nx] > rain_level:    # 다음 지점이 N * N 범위 내부이고, 방문하지 않았으며, 빗물의 높이(레벨)보다 높은 지점이면
                q.append((ny, nx))  # 큐에 enqueue
                visited[ny][nx] = True  # 방문 체크

# 빗물의 높이(레벨) 정보를 바탕으로 안전 영역의 개수를 계산하는 함수
def find_safe_zones(rain_level):
    cnt = 0                 # cnt: 안전 영역의 개수를 저장하는 변수
    for i in range(N):
        for j in range(N):  # 모든 지점을 순회하면서,
            if not visited[i][j] and heights[i][j] > rain_level:    # 방문하지 않은 지점이면서, 빗물의 높이(레벨)보다 높은 지점이면,
                check_safe((i, j), rain_level)  # 해당 지점이 안전 영역이므로 인접한 최대 영역의 안전 영역을 검사
                cnt += 1    # 안전 영역 개수 count
    return cnt              # 모든 지점 검사 후 최종 안전 영역 개수를 반환

# main
N = int(input())    # N: 지역의 크기
heights = [list(map(int, input().split())) for _ in range(N)]   # heights: 높이 정보

min_h = 100     # 지역 내의 최대 높이를 저장할 변수 min_h를 100으로 초기화
max_h = 0       # 지역 내의 최소 높이를 저장할 변수 max_h를 0으로 초기화
for i in range(N):
    for j in range(N):  # 모든 자점을 순회하면서,
        min_h = min(heights[i][j], min_h)   # 최솟값 갱신 후 min_h에 저장
        max_h = max(heights[i][j], max_h)   # 최댓값 갱신 후 max_h에 저장

max_safe_zones = 0      # 안전 영역의 최대 개수를 저장할 변수 max_safe_zones를 0으로 초기화
for rain_level in range(min_h - 1, max_h + 1):  # 빗물의 높이를 최소 높이 ~ 최대 높이까지 변화시키면서,
    visited = [[False] * N for _ in range(N)]   # 검사 방문 정보 초기화
    safe_zones = find_safe_zones(rain_level)    # 빗물의 높이에 따른 안전 영역의 개수를 계산
    max_safe_zones = max(safe_zones, max_safe_zones)    # 안전 영역의 최대 개수 갱신

print(max_safe_zones)   # 검사 종료 후 안전 영역의 최대 개수 출력
