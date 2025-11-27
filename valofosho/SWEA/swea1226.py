"""
미로의 크기 : 16 x 16
1 은 벽 0 은 통로 2는 출발 3은 도착
좌상단 0,0 을 기준으로 가로를 x 세로를 y
시작점은 1,1 -> 사실상 15 x 15 배열
근데 맵을 입력으로 주는거라 16 x 16 -> 인덱스에 조심할 것
도착 가능하면 1
불가능하면 0

"""
from collections import deque
def check(i, j):
    if 1<= i< 15 and 1<= j < 15:
        return True
    else:
        return False

def bfs(i, j):
    visited = [[0] * 16 for _ in range(16)]
    visited[i][j] = 1
    q = deque()
    q.append([i,j])
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    flag = False
    while q:
        i, j = q.popleft()
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if check(ni, nj):
                if maps[ni][nj] == 0 and visited[ni][nj] == 0:
                    q.append([ni,nj])
                    visited[ni][nj] = 1
                elif maps[ni][nj] == 3:
                    flag = True
                    return 1
    if not flag:
        return 0


T = 10 
for test_case in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(16)]
    si, sj = 1, 1
    ans = bfs(si, sj)
    print(f"#{test_case} {ans}")