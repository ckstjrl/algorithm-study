# 일단 늘어난다음 원위치 -> 그대로 구현하기
# 처음엔 오른쪽으로 이동

from collections import deque

# 보드의 크기, 사과의 개수
N, K = int(input()), int(input())    

# 보드 만들기 
# - 패딩을 하고 인덱스범위가 아니라 값을 1로 검사하면 어떨까?

arr = [[0] * (N+2) for _ in range(N+2)]
for i in range(N+2):
    for j in range(N+2):
        if i == 0 or i == N+1:
            arr[i][j] = 1
        if j == 0 or j == N+1:
            arr[i][j] = 1

# 보드에 사과 배치
for _ in range(K):
    i, j = map(int, input().split())
    arr[i][j] = 2


shift = int(input())    # 방향 전환 횟수

# 방향전환정보 튜플 리스트 
turns = [0]*shift
for idx in range(shift):
    sec, direction = input().split()
    turns[idx] = (int(sec), direction)

#우하좌상 방향
way = [[0,1], [1,0], [0,-1], [-1,0]]

# 뱀아 가보자 !
ni, nj = 1,1
snake = deque()
snake.append((1, 1))
to = 0
now_sec = 0
turn_idx = 0

while True:
    # 다음 위치 계산
    ni += way[to][0]
    nj += way[to][1]
    now_sec += 1
    
    # 벽이나 자기 몸에 부딪히면 게임 종료
    if arr[ni][nj] == 1 or (ni, nj) in snake:
        break
    
    # 사과를 먹었는지 확인
    ate_apple = (arr[ni][nj] == 2)
    if ate_apple:
        arr[ni][nj] = 0  # 사과 제거
    
    # 머리 추가
    snake.append((ni, nj))
    
    # 사과를 안 먹었으면 꼬리 제거
    if not ate_apple:
        snake.popleft()
    
    # 방향 전환 체크
    if turn_idx < shift and now_sec == turns[turn_idx][0]:
        direction = turns[turn_idx][1]
        if direction == 'D':
            to = (to + 1) % 4
        else:
            to = (to + 3) % 4
        turn_idx += 1

print(now_sec)