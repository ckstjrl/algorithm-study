"""
BOJ20208 - 진우의 민트초코우유

문제 정의
1. 진우는 진짜 유명한 민초단임
2. NxN 맵에 10개 이하의 민트초코가 산발해있다. 해당 우유를 마시면 체력이 H만큼 는다.
3. 진우가 상하좌우 중 한 칸 움직일 때 마다 체력이 1 줄어듬
4. 체력이 0이되면 진우는 움직일 수 없다.
5. 반드시 집에서 출발해서 집까지 돌아가는데 진우가 마실 수 있는 최대 초코우유 개수를 구하라

로직 정의
1. 어떤 우유를 선택하냐에 따라서 True False 를 나눠서 진행하므로 DFS + HP 상태를 고려한 BackTracking
2. 우선 집과 우유의 위치를 담아둔다.
3. 우유를 마시러 가는 조건은 현재 체력보다 같거나 작은 거리에 우유가 위치해있어야 한다.
4. 만약에 


변수명 정리
1. 집 좌표 -> home = (hi, hj)
2. 민초우 좌표 -> mint[]
3. 체력 -> 초기 : M , 순회 중 -> chp

- 방문을 안했고
- 현재 체력으로 갈 수 있으면 방문
- 집까지 가는 거리가 되면 max_cnt 갱신

"""

import sys
input = sys.stdin.readline

# 두 점 간의 거리를 찾는 맨해튼 거리 리턴
def dist(si, sj, gi, gj):
    return abs(si-gi) + abs(sj-gj)

# 백트래킹 코드
def mincho(si, sj, cnt, chp):
    # 최대 카운트는 글로벌로 유지
    global max_cnt
    # 집까지 거리보다 체력이 크면 집 가능
    if chp >= dist(si,sj, hi,hj):
        max_cnt = max(cnt, max_cnt)
    # 우유 다찾으면 리턴
    if cnt == milk:
        return
    
    for idx, (gi,gj) in enumerate(mint):
        # 아직 마시지 않은 우유
        if not visited[idx]:
            # 갈 수 있는 거리?
            d = dist(si, sj, gi, gj)
            if d <= chp:
                # 방문 처리
                visited[idx] = 1
                # 방문한 척 하고 돌아보기
                mincho(gi,gj, cnt+1, chp-d+H)
                # 사실 우유 안마셨어요
                visited[idx] = 0



N, M, H = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
mint = []
milk = 0
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1: # 집
            hi, hj  = i, j
        elif maps[i][j] == 2: # 우유
            mint.append((i,j))
            milk += 1
max_cnt = 0
# 우유 좌표를 갖는 visited 배열
visited = [0]*(milk+1)
mincho(hi,hj,0,M)
print(max_cnt)