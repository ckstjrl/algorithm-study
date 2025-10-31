"""
BOJ2638 - 치즈

문제 정의
1. NxM 배열, 치즈가 2변 이상 실내 공기랑 접촉하면 녹는다
2. 치즈 내부의 공간은 치즈 외부 공기와 접촉하지 않는 것으로 가정
3. 배열의 가장 자리에는 치즈가 놓이지 않는다
4. 입력으로 주어진 치즈가 모두 녹아 없어지는데 걸리는 시간을 구하라

로직 정의
1. 0,0에서부터 시작해서 공기만 순회
2. 공기에서 각 상하좌우 살피고 공기 & 미방문이면 큐에 삽입
3. 만약 공기에서 치즈를 만나면 해당 치즈 위치를 +1
4. 치즈가 2인 지점을 찾고 0으로 만들기, 치즈 개수 - 해주기
5. 치즈가 0되면 turn 리턴
"""
import sys
import copy
from collections import deque
input = sys.stdin.readline

def check(i,j):
    if 0<=i<N and 0<=j<M:
        return True
    else:
        return False

def bfs(i,j):
    global cz
    q = deque([(i,j)])
    visited[i][j] = True
    temp = 0
    melt = set()
    while q:
        i,j = q.popleft()
        for (di, dj) in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = i+di, j+dj
            if not check(ni,nj): # 범위 밖으로 나가면
                continue
            if visited[ni][nj]: # 이미 방문한 적이 있다면
                continue
            if cz_map[ni][nj] > 0: # 공기 왔다감
                cz_map[ni][nj] += 1
                # 녹일 치즈는 방문처리
                if cz_map[ni][nj] >= 3:
                    melt.add((ni,nj))
                    visited[ni][nj] = True
                
            else:
                visited[ni][nj] = True
                q.append((ni,nj)) # 새로운 공기자리도 넣어주기
    for mi, mj in melt:
        maps[mi][mj] = 0
        cz -= 1
    return cz
        

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
# 우선 치즈를 세볼까요?
cz = 0
for i in range(1,N-1):
    for j in range(1,M-1):
        if maps[i][j] == 1:
            cz += 1
turn = 0
while cz:
    visited = [[False] * M for _ in range(N)]
    turn += 1
    # 딥카피로 다시 바꾸기
    cz_map = copy.deepcopy(maps)
    cz = bfs(0,0)
print(turn)