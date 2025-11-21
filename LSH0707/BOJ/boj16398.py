import sys
import heapq
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
hq = []
visited[0] = 1
for i in range(1, N):
    heapq.heappush(hq, (arr[0][i], i))  # 비용 기준 heappush
ans = 0  # 비용 기록
cnt = 1  # 방문 정점 수 cnt (~N)
while cnt < N:
    w, v = heapq.heappop(hq)  # 최소 비용 간선의 도착지가 방문 기록 없으면 선택
    if visited[v] == 0:
        visited[v] = 1
        ans = ans + w
        cnt = cnt + 1
        for x in range(N):
            if visited[x] == 0:
                heapq.heappush(hq, (arr[v][x], x))
print(ans)
