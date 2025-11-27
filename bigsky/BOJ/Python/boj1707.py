# BOJ1707(D3): 이분 그래프
from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    q = deque([s])
    visited[s] = 1  # 아직 방문하지 않은 곳은 1그룹으로 가정

    while q:
        node = q.popleft()
        for link in graph[node]:
            if not visited[link]:
                q.append(link)
                visited[link] = -visited[node]  # 아직 방문하지 않고 연결되어있는 곳이라면 -1그룹
            elif visited[link] == visited[node]:  # 연결된 곳이 방문한 곳이라면 같은지 검사하고 NO 출력
                return True
    return False

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    # 노드와 간선을 그래프에 저장
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 일단 모든 노드들을 None으로 놓고 나중에 1 or -1로 그룹 정해주기
    visited = [None] * (V + 1)

    # 모든 노드가 방문될 때까지 검사
    for i in range(1, V + 1):
        if not visited[i]:
            if bfs(i):
                print('NO')
                break
    # for문이 정상적으로 다 돌았다면 Yes 출력
    else:
        print('YES')