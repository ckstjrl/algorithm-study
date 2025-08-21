from collections import deque

# 노드 S-G 간 최소 길이 구하기
def bfs(node, s, g, v):
    # 큐, 비지티드 만들고 시작점 넣기
    q = deque()
    visited = [0] * (v+1)
    q.append(s)
    visited[s] = 1   # 시작점 방문 표시

    while q:
        current = q.popleft()

        if current == g:
            return visited[g] -1

        # 현재 노드와 연결된 모든 노드들 확인
        for next in node[current]:
            if visited[next] == 0:
                visited[next] = visited[current] + 1
                q.append(next)

    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V 노드 개수 E 간선 정보
    # 인접 리스트 (각 노드들이 어디랑 인접했는지 표기할거)
    graph = [[] for _ in range(V+1)]

    # 간선 정보를 받자
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    S, G = map(int, input().split())

    ans = bfs(graph, S, G, V)
    print(f"#{tc} {ans}")





