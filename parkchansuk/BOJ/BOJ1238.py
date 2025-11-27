# BOJ 1238. 파티 / D3
'''
문제
N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.

어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다.
이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.

각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다.
하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.

이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다.
N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X가 공백으로 구분되어 입력된다.
두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한 소요시간 Ti가 들어온다.
시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.
모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.

출력
첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력한다.
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N, M, X = map(int, input().split())
graph = [[] for _ in range(M+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((t, e))

INF = 10e9
def dijkstra(star_node):
    pq = [(0, star_node)] # 누적거리, 노드번호
    dists = [0] + [INF] * N # 각 정점까지의 최단 거리를 저장할 리스트
    dists[star_node] = 0 # 시작 노드의 최단 거리는 0

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist: # 이미 저장된 최단 거리가 지금 거리보다 작으면 넘어감
            continue

        for nxt_dist, nxt_node in graph[node]:
            new_dist = dist + nxt_dist

            if dists[nxt_node] <= new_dist:
                continue

            dists[nxt_node] = new_dist
            heappush(pq, (new_dist, nxt_node))

    return dists

X_time = [0]*(N+1) # X_time[i] = i 노드에서 X노드까지의 왕복 시간
lst = [[0]*(N+1)] + [dijkstra(i) for i in range(1, N+1)] # i 노드에서 j 노드로 가는 단시간 이차원 배열

for a in range(1, N+1):
    X_time[a] = lst[a][X] + lst[X][a] # a노드에서 X 노드까지 왕복 시간  = a -> X 단시간 + X -> a 단시간

print(max(X_time))

'''
다익스트라 활용하여 문제 풀이
a -> X 사이의 왕복 시간의 최솟값을 구해야하기 때문에

X_time = [0]*(N+1) # X_time[i] = i 노드에서 X노드까지의 왕복 시간
lst = [[0]*(N+1)] + [dijkstra(i) for i in range(1, N+1)] # i 노드에서 j 노드로 가는 단시간 이차원 배열

for a in range(1, N+1):
    X_time[a] = lst[a][X] + lst[X][a] # a노드에서 X 노드까지 왕복 시간  = a -> X 단시간 + X -> a 단시간
    
이러한 방법을 사용하여 구함
최종적으로 X_time의 max값을 구해 왕복시간의 최댓값을 구함
'''