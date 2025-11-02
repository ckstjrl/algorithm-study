# 2644. 촌수계산

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())                    # 사람 수
a, b = map(int, input().split())    # 촌수 구할 두 사람
M = int(input())                    # 부모-자식 관계 수
graph = [[] for _ in range(N+1)]    # 부모-자식 관계 표현 인접 리스트
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [-1] * (N+1)  # bfs 탐색에 쓸 촌수(거리) 기록; 기본값 -1

# bfs로 그래프 탐색하며 출발 노드에서부터 각 노드까지 방문에 걸린 거리 기록
# 목적지(b) 노드까지 탐색 끝나면 그 노드까지 탐색한 거리(=촌수) 리턴
def bfs(p):
    q = deque([p])
    visited[p] = 0
    while q:
        curr = q.popleft()
        if curr == b:               # b 노드까지 탐색했으면 탐색 종료
            return visited[curr]    # 여기까지 걸린 거리(촌수) 반환
        for nxt in graph[curr]:     # curr과 부모-자식 관계인 노드 nxt
            if visited[nxt] == -1:
                q.append(nxt)
                visited[nxt] = visited[curr] + 1    # 탐색한 거리 +1
    return -1

print(bfs(a))
