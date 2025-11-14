import sys
input = sys.stdin.readline
from collections import deque
N, M, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # 1집, 2우유
hi, hj = 0, 0  # 집 좌표
milk = []  # 우유 좌표
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            hi, hj = i, j
        if arr[i][j] == 2:
            milk.append((i, j))
visited = [0] * len(milk)

def dfs(si, sj, cnt, M):  # (시작i, 시작j, 우유 갯수, 남은 체력)
    global max_milk
    stack = deque()
    stack.append((si, sj, cnt, M))
    while stack:  # dfs
        pi, pj, milk_cnt, hp = stack.pop()
        if abs(pi-hi)+abs(pj-hj) <= hp:  # 해당 좌표에서 집으로 갈 수 있으면 우유 갯수 기록
            if max_milk < milk_cnt:
                max_milk = milk_cnt
        for i in range(len(milk)):  # 우유 좌표 중 방문 기록 없는 곳이면
            if visited[i] == 0:
                ni, nj = milk[i]
                if abs(pi-ni)+abs(pj-nj) <= hp:  # 남은 체력으로 갈 수 있는 곳이면
                    visited[i] = 1  # 백트래킹
                    dfs(ni, nj, cnt+1, hp-(abs(pi-ni)+abs(pj-nj))+H)  
                    # dfs(다음좌표,우유+1, 현재체력-사용한체력+회복한체력)
                    visited[i] = 0

max_milk = 0
dfs(hi, hj, 0, M)
print(max_milk)