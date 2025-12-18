# BOJ 1012. 유기농 배추
'''
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다.
농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에,
한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다.
이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다.
특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어,
그 배추들 역시 해충으로부터 보호받을 수 있다.
한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다.
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면
총 몇 마리의 지렁이가 필요한지 알 수 있다.
'''
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    bat = [[0]*M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        bat[Y][X] = 1

    visited = [[0] * M for _ in range(N)]
    cnt = 0
    while bat != visited:
        for i in range(N):
            for j in range(M):
                if bat[i][j] == 1 and visited[i][j] == 0:
                    q = deque([[i, j]])
                    visited[i][j] = 1

                    while q:
                        ti, tj = q.popleft()
                        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                            ni, nj = ti + di, tj + dj
                            if 0<=ni<N and 0<=nj<M and bat[ni][nj] == 1 and visited[ni][nj] == 0:
                                q.append([ni, nj])
                                visited[ni][nj] = 1
                    cnt += 1
    print(cnt)
    
'''
BFS 사용하여 풀이 진행
밭 이차원 배열과 visited 이차원 배열이 동일해 질때까지 진행
1의 위치를 찾고 그 위치에서 1이 모여있는 덩어리 찾아서 cnt + 1 진행
q가 False가 된 경우 while문이 종료 되면서 cnt + 1이 되고 다시 위로 올라가 1을 찾는 구조
답은 cnt(1모임 덩어리 갯수)
'''