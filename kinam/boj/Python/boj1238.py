'''boj1238 - 파티
N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.

어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다. 
이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.

각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다. 
하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.

이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다. 
N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.
'''
# 최단거리중에 가장 많은 시간 소비?
# 일단 최단거리면 다익스트라
# 오고 가는길이 다를수도있다고 함

'''a가 파티 갔다가 a마을 가기
b가 파티 갔다가 b마을 가기
..... 계속 구하기보다는
각 마을에서 파티마을 가는거랑 
파티마을에서 각 마을까지의 최단거리 구하면 될듯
'''


# + 뒤집은 간선을 이용하면 원래 u -> v(w)인데
# v -> u(w) 이므로, u에서 v로 가는거에서 모든 노드 v에서 u로 오는 걸 구할 수 있다고 함 


from heapq import heappop, heappush
import sys
input = sys.stdin.readline


N, M, X = map(int, input().split())
adj = [[] for _ in range(N + 1)]
reveres_adj = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, time = map(int, input().split())
    adj[start].append((end, time))
    reveres_adj[end].append((start, time))

def dijkstra(start, adj_list):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, now = heappop(pq)
        if d > dist[now]:
            continue
        
        for next_node, cost in adj_list[now]:
            new_dist = d + cost
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heappush(pq, (new_dist, next_node))
    
    return dist

from_x = dijkstra(X, adj)
to_x = dijkstra(X, reveres_adj)

max_time = 0
for i in range(1, N+1):
    total = to_x[i] + from_x[i]
    max_time = max(max_time, total)

print(max_time)