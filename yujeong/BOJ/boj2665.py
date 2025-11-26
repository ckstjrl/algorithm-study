# 2665. 미로만들기

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())    # 미로 크기
maze = [list(map(int, input().rstrip())) for _ in range(N)]     # 미로

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]   # 탐색 4방향

# 다익스트라로 출발점에서부터 (검은 방 통과할 때마다 비용 추가) 도착점까지 탐색
def search(si, sj):
    q = [(0, (si, sj))]     # (비용, (위치x, 위치y))
    cost = [[1e9] * N for _ in range(N)]
    cost[si][sj] = 0

    while q:
        c, (cx, cy) = heappop(q)
        if cx == cy == N-1:     # 도착점 도달하면 비용 리턴 
            return cost[N-1][N-1]
        if c > cost[cx][cy]:
            continue
        for dx, dy in dirs:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N:
                # 방을 지날 때 비용: 검은 방이면 1, 아니면 0
                nxt_cost = 1 if maze[nx][ny] == 0 else 0
                if cost[nx][ny] > cost[cx][cy] + nxt_cost:
                    cost[nx][ny] = cost[cx][cy] + nxt_cost
                    heappush(q, (cost[nx][ny], (nx, ny)))
    return cost[N-1][N-1]

ans = search(0, 0)
print(ans)