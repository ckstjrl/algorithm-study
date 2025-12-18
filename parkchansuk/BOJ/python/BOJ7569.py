# BOJ 7569. 토마토
'''
창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다.
M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다.
단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다.
둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다.
즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다.
각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다.
정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
이러한 N개의 줄이 H번 반복하여 주어진다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다.
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고,
토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
'''

import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

q = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == 1:
                q.append([h, i, j])

if not any(0 in row for layer in box for row in layer):
    print(0)
    sys.exit() # 조건 만족되면 아예 정지
# for layer in box:
#     for row in layer:
#         if 0 not in row:
#             print(0)
#             sys.exit()
# 이렇게 작성했더니 틀렸다 연산함. chatGPT에게 물어보니 0이 없는 행이 발견되면 바로 넘어가서 문제라고 함

while q:
    sh, si, sj = q.popleft()
    for dh, di, dj in [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]:
        th, ti, tj = sh + dh, si + di, sj + dj
        if 0<= th < H and 0<= ti < N and 0<= tj < M and box[th][ti][tj] == 0:
            box[th][ti][tj] = box[sh][si][sj] + 1
            q.append([th, ti, tj])


if any(0 in row for layer in box for row in layer):
    print(-1)
    sys.exit() # 조건 만족되면 아예 정지


else:
    ans = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if ans < box[h][i][j]:
                    ans = box[h][i][j]
    print(ans - 1)

'''
3차원 배열로 입력을 받아서 진행
3차원 배열의 경우 arr[높이][행][렬] 이런 식으로 인덱스 주어짐
최소 날자를 원하는 것을 봐 BFS라 생각하고 풀이 진행
한번에 익은 토마토의 좌표를 받아서 deque애 집어 넣고 풀이를 진행해야 익은 토마토가 여러 개 일때 병렬 진행 가능
visited를 설정하고 풀이할까 생각했는데
if 절에서 box[th][ti][tj] == 0 을 사용하면서 visited가 의미가 없어짐
(box의 원소값이 달라지면 그 곳에 다시 방문하지 않기 때문)
대신 box[th][ti][tj] = box[sh][si][sj] + 1 를 사용해서 다 익는 날짜짜를 구함
box에서 가장 큰 값에서 -1을 진행하면 다 익는 날짜를 구할 수 있음
'''