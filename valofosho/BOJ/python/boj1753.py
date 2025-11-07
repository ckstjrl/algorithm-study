"""5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6"""
import heapq
import sys
input = sys.stdin.readline
def dijkstra(start_node):
    pq = [(0,start_node)]
    # 시작점 초기화
    dists[start_node] = 0
    while pq:
        dist, node = heapq.heappop(pq)
        # 이미 더 작은 값으로 왔으면 버리기
        if dists[node] < dist:
            continue
        # 이게 더 작으면!
        for nx_dist, nx_node in adj[node]:
            # 다음 노드로 가는 누적 거리 계산
            new_dist = dist + nx_dist
            if new_dist < dists[nx_node]:
                dists[nx_node] = new_dist
                heapq.heappush(pq, (new_dist, nx_node))


V, E = map(int, input().split())
INF = float('INF')
adj = [[] for _ in range(V+1)]
start_node = int(input())
dists = [INF] * (V+1)

for i in range(E):
    s, g, w = map(int, input().split())
    # 다익스트라는 단방향
    adj[s].append((w,g))
dijkstra(start_node)
for i in dists[1:]:
    if i != INF:
        print(i)
    else:
        print('INF')