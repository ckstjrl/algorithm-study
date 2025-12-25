import sys
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
x, y = map(int, input().split())

cost = [float('inf')] * (N+1)  # 최소 비용 기록
cost[x] = 0
hq = []
heapq.heappush(hq, (0, x))  # (비용, 위치)
while hq:
    c, now = heapq.heappop(hq)
    if cost[now] < c:  # 기록된 값이 더 작으면 continue
        continue
    for nxt, w in arr[now]:
        if cost[nxt] > c + w:  # 다음도시 최솟값 갱신 가능하면
            cost[nxt] = c + w
            heapq.heappush(hq, (cost[nxt], nxt))  # heapa에 추가

print(cost[y])
