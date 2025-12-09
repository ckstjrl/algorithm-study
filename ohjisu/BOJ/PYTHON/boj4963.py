import sys
input  = lambda :sys.stdin.readline().rstrip()
from collections import deque

DIRS = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]

def is_valid(i, j, h, w):
    return 0 <= i < h and 0 <= j < w

def find_island(i, j, graph):
    return graph[i][j] == 1

def find_answer(w, h):
    graph = [list(map(int, input().split())) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if not find_island(i, j, graph):
                continue
            if visited[i][j]:
                continue
            cnt += 1
            visited[i][j] = 1
            q = deque([(i, j)])
            while q:
                si, sj = q.popleft()
                for di, dj in DIRS:
                    ni, nj = si + di, sj + dj
                    if not is_valid(ni, nj, h, w):
                        continue
                    if visited[ni][nj]:
                        continue
                    if not find_island(ni, nj, graph):
                        continue
                    visited[ni][nj] = 1
                    q.append((ni, nj))

    print(cnt)

def user_input():
    return map(int, input().split())

w, h = user_input()
while w != 0 and h != 0:
    find_answer(w, h)
    w, h = user_input()




