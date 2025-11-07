# 6087. 레이저 통신

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

W, H = map(int, input().split())    # 가로 W칸, 세로 H칸
grid = [list(input()) for _ in range(H)]    # 지도
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]   # 인접 방향 
INF = 1e9

c_pos = []  # 'c'로 표시된 칸 위치 2개를 저장할 리스트
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'C':
            c_pos.append((i, j))

# 다익스트라로 첫 번째 c -> 두 번째 c 탐색하며 필요한 거울의 최소 개수를 구하기
def search(si, sj):
    # 탐색을 위한 우선순위 큐 q
    q = []      # 우선순위 큐에 저장되는 것: (거울 개수, 칸 좌표, 진입 방향)

    # 각 칸마다 4개 진입 방향별 최소비용 기록할 3차원 리스트 cost
    cost = [[[INF] * 4 for _ in range(W)] for _ in range(H)]    

    # 시작 좌표 기준 초기화: 모든 방향에서 비용 0
    for d in range(4):
        cost[si][sj][d] = 0
        heappush(q, (0, (si, sj), d))
    
    while q:
        cnt, (cx, cy), curr_d = heappop(q)  # (cx, cy) 도달을 위한 거울 개수 cnt와 그때 진입 방향 curr_d

        # 목적지 C칸에 도달
        if (cx, cy) == (ei, ej):
            return cost[ei][ej][curr_d]     # 지금까지의 최소 거울 개수 리턴

        # cnt가 기존 최소비용보다 크면 continue
        if cnt > cost[cx][cy][curr_d]:
            continue
        
        # (cx, cy)에서 인접한 4개 방향별로
        for nxt_d in range(4):
            nx, ny = cx+dirs[nxt_d][0], cy+dirs[nxt_d][1]
            if 0<=nx<H and 0<=ny<W and grid[nx][ny]!='*':       # 유효한 인덱스인 경우
                nxt_cnt = cnt if nxt_d == curr_d else cnt + 1   # 방향이 달라지면 거울 개수 +1
                if nxt_cnt < cost[nx][ny][nxt_d]:   # 기존 비용보다 더 작아졌으면 비용 갱신하고 큐에 추가
                    cost[nx][ny][nxt_d] = nxt_cnt
                    heappush(q, (nxt_cnt, (nx, ny), nxt_d))
    return -1

si, sj = c_pos[0]   # 첫 번째 'c'칸 좌표 (여기서 출발)
ei, ej = c_pos[1]   # 두 번째 'c'칸 좌표 (여기로 도착)

print(search(si, sj))   # 탐색하고 결과 출력
