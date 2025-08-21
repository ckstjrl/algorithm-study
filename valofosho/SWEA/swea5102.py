"""
V 노드, E 간선 (방향 없음 -> 양방향이라 생각)


"""
from collections import deque

def bfs(S,G, V):
    visited = [0] * (V+1)
    visited[S] = 1
    q = deque()
    q.append(S)
    while q:
        cur = q.popleft()
        for link in adj[cur]:
            if visited[link] == 0:
                visited[link] = visited[cur] + 1
                q.append(link)
    return visited[G] -1 if visited[G] != 0 else 0

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)
    S, G = map(int, input().split())
    ans = bfs(S,G, V)
    print(f"#{test_case} {ans}")