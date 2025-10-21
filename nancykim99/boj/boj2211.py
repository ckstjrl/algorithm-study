'''
BOJ221 / D3): 네트워크 복구

해결 방법 : 다익스트라로 최저 경로와 경로에서 사용한 회선 추가.
1. 각 노드의 부모 노드를 저장하고, 최단 경로가 갱신될때마다 부모 노드를 기록하기.
2. 복구된 회선을 set으로 중복 제거함
3. 1번 컴퓨터를 제외한 다른 컴퓨터들을 순회하면서, 만약 부모가 있으면 회선을 추가

메모 :
`parent = [0] * (N+1)`
`parent[next_node] = node`
이 방법을 통해 복구한 회선 추가하기
'''

from heapq import heappop, heappush

def dijkstra(start): 
    pq = [(0, start)] # (누적거리, 노드번호)
    dists = [INF] * (N + 1) # 각 정점까지의 최단거리를 저장할 리스트 / 누적거리합리스트
    dists[start] = 0 # 시작노드에서 시작노드의 최단거리는 당연히 0

    parent = [0] * (N + 1)
 
    while pq:
        dist, node = heappop(pq) # 시작점부터 거리와 노드번호 꺼내기
        if dists[node] < dist: # 만약 이 노드의 최단거리가 지금 가져온 누적거리보다 작으면, 지금 가져온 누적거리가 필요없기에
            continue # 버리기
        for next_node, next_dist in graph[node]:
            new_dist = next_dist + dist
            if dists[next_node] <= new_dist:
                continue
            dists[next_node] = new_dist
            parent[next_node] = node
            heappush(pq, (new_dist, next_node))
 
    return parent


N, K = map(int, input().split())

start = 0
INF = int(21e8)

# 인접 리스트 만들기
graph = [[] for _ in range(N + 1)]
for _ in range(K):
    s, e, w = map(int, input().split())
    graph[s].append((e, w)) # 양방향
    graph[e].append((s, w)) # 양방향

result = dijkstra(1)

recovered_lines = set()
for i in range(1, N + 1):
    if result[i] != 0 and result[i] != i:
        line = tuple(sorted((i, result[i])))
        recovered_lines.add(line)

print(len(recovered_lines))
for s, e in sorted(list(recovered_lines)):
    print(s, e)