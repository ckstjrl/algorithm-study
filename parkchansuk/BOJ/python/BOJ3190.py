#BOJ 3190. 뱀 / D3
'''
'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다.
뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다.
보드의 상하좌우 끝에 벽이 있다.
게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다.
뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())

# 보드: 사과=1, 없음=0
arr = [[0]*N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

L = int(input().strip())
# time-indexed 회전 정보: 'L' or 'D'
move = [''] * 10001   # 시간 t가 곧 인덱스 (여유 있게)
for _ in range(L):
    t, v = input().split()
    T = int(t)
    move[T] = v

# 방문(몸체) 표시와 뱀 몸 좌표
visited = [[0]*N for _ in range(N)]
snake = deque([(0, 0)])   # 머리를 맨 뒤로 두자
visited[0][0] = 1

# 방향: 오른쪽, 아래, 왼쪽, 위 (시계방향)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
d_idx = 0  # 처음엔 오른쪽

time = 0
i, j = 0, 0  # 현재 머리 위치

while True:
    time += 1
    ni, nj = i + di[d_idx], j + dj[d_idx]

    # 벽 or 자기 몸과 충돌 -> 종료
    if not (0 <= ni < N and 0 <= nj < N) or visited[ni][nj] != 0:
        print(time)
        break

    # 머리 전진
    snake.append((ni, nj))
    visited[ni][nj] = 1

    # 사과 처리
    if arr[ni][nj] == 1:
        arr[ni][nj] = 0   # 사과 먹으면 꼬리 그대로(길이+1)
    else:
        ti, tj = snake.popleft()  # 사과 없으면 꼬리 이동
        visited[ti][tj] = 0

    i, j = ni, nj

    # t초가 지난 '직후' 회전
    if move[time]:
        if move[time] == 'L':
            d_idx = (d_idx - 1) % 4
        else:  # 'D'
            d_idx = (d_idx + 1) % 4

'''
visited로 뱀의 몸과 움직임 표현
덱으로 꼬리를 pop하고 머리를 append(visited 좌표)
과거 달팽이 숫자 문제처럼 4로 나눠주면서 방향 제공
한번 움직일때마다 time 증가
time을 인덱스로 해서 회전정보 확인
'''