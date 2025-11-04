'''boj1753 최단경로

방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 
단, 모든 간선의 가중치는 10 이하의 자연수이다.

첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. 
(1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 
둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 
셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. 
u와 v는 서로 다르며 w는 10 이하의 자연수이다. 
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
'''

# 다른 모든 정점으로의 최단 경로?? -> Dijkstra?

def dijkstra(start):
    pq = [(0, start)] # (누적거리, 노드 번호)
    distances = [float('inf')] * (V + 1) # 각 정점까지의 최단거리를 저장할 리스트
    distances[start] = 0  # 시작노드의 최단거리는 0

    while pq:
        distance, node = heappop(pq)

        # 이미 더 작은 값으로 온 적이 있으면 버림
        if distances[node] < distance:
            continue

        for next_distance, next_node in graph[node]: #node의 인접리스트를 순회
            # 다음 노드에 저장할 누적 거리
            new_distance = distance + next_distance

            # 이미 크거나 같은 가중치로 온 적이 있다면 continue
            if distances[next_node] <= new_distance:
                continue

            #누적거리, 새로운 노드를 pq에 저장 + distances에 갱신
            distances[next_node] = new_distance
            heappush(pq, (new_distance, next_node))
    
    return distances


from heapq import heappop, heappush

V, E = map(int, input().split()) #정점의 개수 V, 간선의 개수 E
K = int(input()) #시작 정점의 번호

graph = [[] for _ in range(V + 1)] # 인접 리스트 생성

for _ in range(E):
    u, v, w = map(int, input().split())

    #u에서 v로 감. u의 인접 리스트에 weight, v 를 추가
    graph[u].append((w, v))

#출발지로부터 모든 최단 거리
ans = dijkstra(K)

for i in range(1, len(ans)):
    if ans[i] == float('inf'):
        ans[i] = 'INF'
    print(ans[i])



