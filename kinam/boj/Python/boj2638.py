'''boj2638 - 치즈
N×M의 모눈종이 위에 아주 얇은 치즈가 <그림 1>과 같이 표시되어 있다. 
단, N 은 세로 격자의 수이고, M 은 가로 격자의 수이다. 
이 치즈는 냉동 보관을 해야만 하는데 실내온도에 내어놓으면 공기와 접촉하여 천천히 녹는다. 
그런데 이러한 모눈종이 모양의 치즈에서 각 치즈 격자(작 은 정사각형 모양)의 4변 중에서 적어도 2변 이상이 실내온도의 공기와 접촉한 것은 정확히 한시간만에 녹아 없어져 버린다. 
따라서 아래 <그림 1> 모양과 같은 치즈(회색으로 표시된 부분)라면 C로 표시된 모든 치즈 격자는 한 시간 후에 사라진다.

0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0
0 0 0 0 0 1 1 0
0 0 1 0 0 0 0 0
0 0 0 1 1 0 1 0
0 1 1 0 0 1 1 0
0 0 0 0 0 0 0 0
그림 1

0 0 0 0 0 0 0
0 0 1 1 0 1 1
0 0 0 0 0 0 0
0 0 0 1 0 0 0
0 0 1 1 0 1 1
0 0 0 0 0 0 0
0 0 0 0 0 0 0
그림2

<그림 2>와 같이 치즈 내부에 있는 공간은 치즈 외부 공기와 접촉하지 않는 것으로 가정한다. 그러므 로 이 공간에 접촉한 치즈 격자는 녹지 않고 C로 표시된 치즈 격자만 사라진다. 그러나 한 시간 후, 이 공간으로 외부공기가 유입되면 <그림 3>에서와 같이 C로 표시된 치즈 격자들이 사라지게 된다.


0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 1 0 1 0 1 0
0 0 1 0 1 0 0
0 1 0 1 0 1 0
0 1 0 0 1 0 0
0 0 0 0 0 0 0
그림3


모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정한다. 입력으로 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 구하는 프로그램을 작성하시오.
'''

'''
빙산과 비슷한 문제 boj2573 - 빙산
-> 녹는 로직을 마지막에 한번에 적용해야함. 
중간중간에 녹아서 공기인걸로 치면 다음 인덱스의 치즈가 주변 인접 공기 확인할때 문제생김

치즈 안쪽의 공기를 어떻게 구분할 것인가?
치즈 안쪽의 공기는 같은 공기여도 안녹는 공기임

-> 시작 인덱스 (0, 0)부터 bfs를 진행해서 visited처리를 해줌.
치즈는 벽으로 생각하고 visited 안해버리면?
최종 bfs 끝나고 나면 치즈 안쪽의 공기의 값도 visited값은 0일 것임
치즈 바깥의 공기 visited값은 1일 것임

따라서 현재 칸이 치즈인데 인접칸이 visited[ni][nj] == 1 일때만 치즈랑 닿는 녹는공기임 cnt 1늘리고
cnt 2 이상되면 녹는걸로 
'''



import sys
from collections import deque

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

cheese_cnt = 0 #치즈 갯수

for i in range(N):
    for j in range(M):
        if cheese[i][j] == 1:
            cheese_cnt += 1

# print(f"cheese_cnt : {cheese_cnt}")

ans = 0
while cheese_cnt > 0:
    air = [[0] * M for _ in range(N)]
    melt = [[0] * M for _ in range(N)]

    #0,0부터 bfs를 갈겨서 visited(air)값이 0이면 cheese 또는 cheeese air인거임
    q = deque([(0, 0)])
    air[0][0] = 1

    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            # 범위조건, 공기방문처리, 치즈가 아니어야함
            if 0 <= ni < N and 0 <= nj < M and not air[ni][nj] and not cheese[ni][nj]:
                q.append((ni, nj))
                air[ni][nj] = 1

    for i in range(N):
        for j in range(M):
            air_cnt = 0
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                # 인접 2곳이 공기면?
                if 0 <= ni < N and 0 <= nj < M and air[ni][nj] == 1:
                    air_cnt += 1
            if cheese[i][j] == 1 and air_cnt >= 2:
                melt[i][j] = 1
    
    # 녹아야할 치즈 한번에 녹게 함
    for i in range(N):
        for j in range(M):
            if melt[i][j] == 1:
                cheese[i][j] = 0
                cheese_cnt -= 1
    
    # print(f"cheese_cnt : {cheese_cnt}")
    
    ans += 1

print(ans)