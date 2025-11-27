"""
지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.
입력
지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)
다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.
출력
각 지점에서 목표지점까지의 거리를 출력한다.
원래 갈 수 없는 땅인 위치는 0을 출력하고, # visited[i][j] == 0 but maps[i][j] == 0 -> 0
원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다. # -> visited[i][j] == 0 and maps[i][j] == 1 -> -1

순회를 두 번 해야 한다는 문제가 있긴 하다
우선 풀어보고 다시 또 생각하기!
"""

from collections import deque

def check(i, j, N, M):
    if 0<=i<N and 0<=j<M and maps[i][j] == 1:
        return True
    else:
        return False

def find_start(N,M):
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 2:
                return i, j

def postifx():
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and maps[i][j] == 1:  # 방문한 적이 없지만 갈 수 있는 길이면
                visited[i][j] = -1  # -1로 바꿔주기
    return visited

def bfs(i,j):
    visited = [[0]* M for _ in range(N)]
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    q = deque()
    q.append([si,sj])
    while q:
        i, j = q.popleft()
        for d in range(4):
            ni,nj = i+di[d], j+dj[d]
            if check(ni,nj, N, M):    # 범위 내에서의 이동인지
                if visited[ni][nj] == 0:     # 방문을 한 적이 없는지
                    visited[ni][nj] = visited[i][j] + 1     # 이전까지의 거리 + 1 저장
                    q.append([ni,nj])
    return visited


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
si, sj = find_start(N,M)
visited = bfs(si,sj)
answer = postifx()
for row in answer:
    print(*row)