# 3190. 뱀

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())    # 보드 크기 N x N
K = int(input())    # 사과의 개수

# 0이면 빈칸, 1이면 사과, 2면 뱀
board = [[0]*N for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())    # 사과 위치
    board[x-1][y-1] = 1                 

cd = [0] * 10001
L = int(input())    # 방향 전환 횟수
for _ in range(L):
    n, d = input().split()
    cd[int(n)] = d



snake = deque([(0, 0)])   # 인덱스 큰쪽이 머리 작은쪽이 꼬리 
px, py = 0, 0             # 출발 위치

sec = 0     # 초
d = 0       # 방향 전환용 인덱스 
dx = [0, 1, 0, -1]  # 오른쪽 - 아래 - 왼쪽 - 위 순 
dy = [1, 0, -1, 0]

while True:
    sec += 1            # 시간 +1
    nx = px + dx[d]     # 다음 이동할 곳 
    ny = py + dy[d]

    # 뱀이 벽 또는 자기 몸에 부딪히는 경우 break
    if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] == 2:
        break
    
    if board[nx][ny] == 1:  # 사과 있음
        pass
    else:                   # 사과 없음
        tx, ty = snake.popleft()
        board[tx][ty] = 0   # 꼬리 줄이기
    
    # 뱀 머리 이동 표시
    board[nx][ny] = 2
    snake.append((nx, ny))
    px, py = nx, ny

    # 방향 전환해야 하는 경우 전환 
    if cd[sec]:
        if cd[sec] == 'D':  # 오른쪽으로 90도
            d = (d+1) % 4
        else:               # 왼쪽으로 90도 
            d = (d+3) % 4

print(sec)