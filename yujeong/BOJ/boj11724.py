# 11724. 연결 요소의 개수

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())    # 노드 개수 N, 간선 개수 M

graph = [[] for _ in range(N+1)]    # 인접 리스트 만들기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


cnt = 0     # 연결 요소 개수 저장 
visited = [False] * (N+1)   # 방문 여부 저장

# 그래프를 bfs로 탐색하며 방문 여부 갱신
def bfs(s):
    q = deque([s])
    visited[s] = True
    while q:
        curr = q.popleft()
        for nxt in graph[curr]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
    return

# 1번부터 N번까지 순서대로 노드 탐색하며
for i in range(1, N+1): 
    if not visited[i]:  # 아직 방문하지 않은 노드면
        cnt += 1        # 연결 요소 개수 +1
        bfs(i)          # bfs로 이 노드에서부터 연결된 노드들 탐색 시작

print(cnt)
