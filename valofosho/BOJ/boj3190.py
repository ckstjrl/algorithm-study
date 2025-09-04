"""
뱀
뱀의 초기 위치는 0,0
초기 길이는 1
보드는 N X N
보드의 상하좌우 끝에 벽
뱀의 이동 규칙
1. 뱀의 몸 길이를 늘려 다음 칸에 위치
2. 만약 벽이나 자기 자신과 몸이 부딛히면 게임오버
3. 이동한 칸에 사과가 있다면 먹고 꼬리는 움직이지 않는다
4. 이동한 칸에 사과가 없다면 몸 길이를 줄여서 꼬리가 위치한 칸을 비워준다.

사과의 개수 K
사과, 뱀 좌표 모두 1-based 인덱스
방향 변환 횟수 L
정수 X와 문자 C X초 끝나고 L or D (90도 회전)

로직 정의
1. 사과의 먹는 순서는 중요하지 않다
2. 사과는 map에 표시하기!
3. L줄동안 이어지는 초표시는 그 전까지 직진만 하라는 뜻
4. 뱀의 몸 길이를 어떻게 표현할 지가 가장 큰 문제
    -> 만약에 몸의 길이를 표현하는 visited 배열을 하나 만들고
    -> 몸의 길이가 들어있는 deque을 하나 선언한다
    -> 움직이고 없으면 덱에서 popleft()로 꼬리 떼어네기
    -> popleft를 visited에서 다시 0으로 만들어주기
5. 3초라는 건 1, 2, 3 총 3번 이동 후 진행방향을 바꿔주는 것
    -> di, dj를 순차적으로 진행한다고 가정하고 %로 델타 바꿔주기

6. 어차피 이동하는 방향은 정해져있으므로 BFS처럼 나눠서 가는게 X
시뮬레이션 처럼 주어진 방향성만 유지하면서 사과가 모두 사라지는 시점을 구하는 문제
그러면 사과도 deque을 하나 만들어줘

문제 풀이 나누기
1. 뱀의 몸을 담는 snake = deque([0,0]) <- 초기 위치
2. apple은 먹은 cnt를 하나 만들고 하는게 나아요
3. 초에 관한 문제는 큐에서 하나하나 빼면서 하고 break
이래 끝나나 저래 끝나나 초 반환

"""

from collections import deque

# 벽 바깥으로 나가는지 체크 -> 나가면 break
def check(i,j):
    if 0<=i<N and 0<=j<N:
        return True
    else:
        return False
    
# 머리 돌리기
def turn_head(cur, cmd):
    if cmd == 'D':
        temp = (cur + 1) % 4
    else:
        temp = (cur + 3) % 4
    return temp

def move():
    snake = deque()
    snake.append([0,0])
    body = [[0] * N for _ in range(N)] # 몸의 위치 표시 맵
    body[0][0] = 1  # 시작점 방문 처리
    di = [0, 1, 0, -1]
    dj = [1, 0 , -1, 0]
    sec = 0
    cnt = 0
    d = 0
    while True:
        sec += 1
        snake_head = snake.popleft()
        i, j = snake_head[0], snake_head[1]
        ni, nj = i+di[d], j+dj[d]
        if check(ni,nj) and body[ni][nj] == 0:
            if maps[ni][nj] == 1:
                # 몸을 늘린다 = 기존 머리를 치우지 않는다
                snake.appendleft(snake_head)
                # 머리 추가 이동
                snake.appendleft([ni,nj])
                # 몸통에 추가해주기
                body[ni][nj] = 1
                cnt += 1
                maps[ni][nj] = 0

            else:
                # 빼낸 머리 다시 넣어주고
                snake.appendleft(snake_head)
                # 새 머리 이동
                snake.appendleft([ni,nj])
                body[ni][nj] = 1
                # 꼬리 빼주기
                tail_i, tail_j = snake.pop()
                # 바디에서 없애주기
                body[tail_i][tail_j] = 0
        else:
            return sec

        # 시간 초 지나면 방향 바꾸기
        if cmd:
            check_sec = cmd.popleft()
            if sec == check_sec[0]:
                d = turn_head(d, check_sec[1])
            else:
                cmd.appendleft(check_sec)



N = int(input())
K = int(input())
maps = [[0]* N for _ in range(N)]

# K는 사과의 개수
for _ in range(K):
    i, j = map(int, input().split())
    maps[i-1][j-1] = 1

# 이동 명령은 L 개
L = int(input())

# 시간 별 이동 순서를 담는 명령 큐
cmd = deque()
for _ in range(L):
    sec, dir = input().split()
    cmd.append([int(sec), dir])

ans = move()
print(ans)
