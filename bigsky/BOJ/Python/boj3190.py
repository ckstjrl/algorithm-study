# 백준3190(D3) : 뱀
from collections import deque

N = int(input())  # 보드의 크기
K = int(input())  # 사과의 개수
a_lst = set(tuple(map(int, input().split())) for _ in range(K))  # 사과의 위치
L = int(input())  # 뱀의 방향전환 횟수
d_lst = [input().split() for _ in range(L)]

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]  # 델타 정의
d_tb = [0] * 10001  # 방향전환 테이블
for sec, turn in d_lst:
    d_tb[int(sec)] = turn

direction = 0
snake = deque([(1, 1)])
ans = 0  # 초(sec)가 누적됨

while True:
    ans += 1
    si, sj = snake[-1]
    ni, nj = si + di[direction], sj + dj[direction]
    # 벽에 부딪히거나, 몸에 부딪힌 경우 종료
    if 0 < ni <= N and 0 < nj <= N and (ni, nj) not in snake:
        # 머리 이동
        snake.append((ni, nj))
        # 사과를 먹었다면 사과 먹기 & 꼬리는 남기기
        if (ni, nj) in a_lst:
            a_lst.remove((ni, nj))
        # 사과를 안먹었다면 꼬리 제거
        else:
            snake.popleft()
        # 방향전환
        if d_tb[ans] == 'D':
            direction = (direction + 1) % 4
        elif d_tb[ans] == 'L':
            direction = (direction + 3) % 4     
    else:
        break

print(ans)