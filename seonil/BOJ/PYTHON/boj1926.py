"""
BOJ1926. 그림

[문제]
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라.
 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자.
 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

[입력]
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다.
두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

[출력]
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

# 상하좌우 델타 배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# BFS 탐색 함수: 시작 좌표에서 연결된 1들의 넓이를 구함
def check_picture(start):
    global cnt_pictures  # 전체 그림 수를 세는 전역 변수
    sy, sx = start

    # 시작점이 0이면 그림이 아님
    if paper[sy][sx] == 0:
        return 0
    else:
        q = deque([start])  # BFS를 위한 큐
        visited[sy][sx] = True  # 시작점 방문 체크
        cnt_pictures += 1  # 그림 개수 하나 추가
        cnt_area = 1  # 현재 그림 넓이 1로 시작

        # BFS 시작
        while q:
            y, x = q.popleft()
            for dir in range(4):  # 상하좌우 네 방향 탐색
                ny, nx = y + dy[dir], x + dx[dir]
                # 다음 좌표가 범위 내에 있고, 아직 방문하지 않았으며, 값이 1인 경우,
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and paper[ny][nx] == 1:
                    q.append((ny, nx))  # 큐에 다음 좌표 enqueue
                    cnt_area += 1   # 넓이 1칸 늘리기
                    visited[ny][nx] = True  # 다음 좌표 방문 체크

    return cnt_area  # BFS 탐색 완료 후 현재 그림의 넓이 반환

# main
n, m = map(int, input().split())    # n: 행 개수, m: 열 개수
paper = [list(map(int, input().split())) for _ in range(n)] # 도화지 입력 받기
visited = [[False] * m for _ in range(n)]   # 방문 여부 저장 배열

cnt_pictures = 0  # 전체 그림 수
max_area = 0      # 가장 큰 그림 넓이

# 모든 도화지 셀에 대해 탐색
for i in range(n):
    for j in range(m):
        if not visited[i][j]:  # 아직 방문하지 않았다면
            area = check_picture((i, j))  # BFS로 그림의 넓이 구함
            max_area = max(area, max_area)  # 최대 넓이 갱신

# 출력: 그림 수, 가장 큰 그림의 넓이
print(cnt_pictures)
print(max_area)
