# BOJ 1238. 파티 (G3 / D3)
import heapq

n, m, x = map(int, input().split())

# 정방향, 역방향 그래프
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    reverse_graph[b].append((a, t))

def dijkstra(start, adj):
    # 다익스트라로 start에서 모든 노드까지 최단거리
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        d, node = heapq.heappop(heap)
        
        if d > dist[node]:
            continue
        
        for next_node, cost in adj[node]:
            new_dist = d + cost
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))
    
    return dist

# X에서 각 마을로 돌아가는 최단거리
go_home = dijkstra(x, graph)

# 각 마을에서 X로 가는 최단거리 (역방향 그래프 사용)
go_party = dijkstra(x, reverse_graph)

# 왕복 시간 최댓값
max_time = 0
for i in range(1, n + 1):
    max_time = max(max_time, go_party[i] + go_home[i])

print(max_time)