'''
BOJ1238 / D3): 파티

N == N명의 학생 == N개의 마을 == 노드의 개수
M == M개의 단방향 도로 == 간선의 개수
X == 학생들이 모일 마을 == 마지막 노드 번호

해결방법 : 단방향 다익스트라.
1. 각 학생마다 다익스트라를 해서 최저경로를 찾고, 그 최저경로 X 2 하는 식으로 왕복을 구해봄 -> 최저 왕복 거리가 나오지 않음
2. 각 학생마다 다익스트라를 하고, 거꾸로 도착점에서 각 노드까지 최저 경로를 찾고 그 리스트에서 각 학생들이 갈때, 올때 최저경로 더함 -> 최저 왕복 거리는 나오나, 시간이 너무 오래걸림
3. 단방향 리스트를 거꾸로 만들어서, 다익스트라 진행. 그리고 기존 리스트로 역다익스트라 진행. 가는 최단경로와 오는 최단 경로 구해서 더하기.
    * 단방향일때, 다익스트라를 모든 노드에서 돌려야 하고, 도착점이 정해져 있다면, 도착점에서 시작점으로 가는 역리스트를 만들어서 그 역리스트로 다익스트라를 돌리는 것이 더 효율적이다...!
'''

from heapq import heappop, heappush

def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * (N+1)
    dists[start_node] = 0
    while pq:
        dist, node = heappop(pq)
        if dists[node] < dist:
            continue
        for next_dist, next_node in graph_rev[node]:
            new_dist = next_dist + dist
            if dists[next_node] <= new_dist:
                continue
            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))
    
    return dists

def rev_dijkstra(end_node):
    pq = [(0, end_node)]
    dists = [INF] * (N+1)
    dists[end_node] = 0
    while pq:
        dist, node = heappop(pq)
        if dists[node] < dist:
            continue
        for next_dist, next_node in graph[node]:
            new_dist = next_dist + dist
            if dists[next_node] <= new_dist:
                continue
            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))
    
    return dists

N, M, X = map(int, input().split())
INF = int(21e8)
graph = [[] for _ in range(N+1)] # 인접리스트
graph_rev = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end)) # 단방향
    graph_rev[end].append((weight, start)) # 거꾸로 단방향

dists_back = rev_dijkstra(X)
dists_go = dijkstra(X)

student_dist = 0
for i in range(1, N+1):
    student = dists_go[i] + dists_back[i]
    if student > student_dist:
        student_dist = student

    
print(student_dist)
