import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
arr = [[0] * N for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
tmp_list = [list(map(int, sys.stdin.readline().split())) for _ in range(K)] # 사과의 위치를 담을 임시 리스트
for i in range(K):
    arr[tmp_list[i][0] - 1][tmp_list[i][1] - 1] = 2 # 사과의 위치 2로 표시
L = int(input())

info = [] # 방향 정보 담을 리스트
for i in range(L):
    x, c = sys.stdin.readline().split()
    info.append([int(x), c]) # 시간 값은 정수로 받음

x, y = 0, 0 # 초기 위치
arr[x][y] = 1 # 뱀
clock = 0
dir = 0
queue = deque()
queue.append((0, 0))

def turn(clk): # 방향 전환
    global dir
    if clk == 'L':
        dir = (dir - 1) % 4
    else:
        dir = (dir + 1) % 4

while True:
    clock += 1
    x += dx[dir]
    y += dy[dir]
    if x < 0 or x >= N or y < 0 or y >= N: # 뱀 머리가 벽에 닿는다면
        break
    if arr[x][y] == 2: # 사과를 만난다면
        arr[x][y] = 1
        queue.append((x, y)) # 뱀 길이 +
        for i in range(L):
            if clock == info[i][0]: # 방향 정보의 시간과 같아진다면
                turn(info[i][1]) # 방향 전환
    elif arr[x][y] == 0: # 사과가 없다면
        arr[x][y] = 1
        queue.append((x, y)) # 뱀 길이 +
        tx, ty = queue.popleft() # 뱀 길이 -
        arr[tx][ty] = 0
        for i in range(L):
            if clock == info[i][0]: # 방향 정보의 시간과 같아진다면
                turn(info[i][1]) # 방향 전환
    else:
        break

print(clock)