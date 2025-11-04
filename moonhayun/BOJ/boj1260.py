# [문제]
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# [입력]
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
# 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# [출력]
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
# V부터 방문된 점을 순서대로 출력하면 된다.

import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
tree = [[] for _ in range(N + 1)]

for _ in range(M):
    s, g = map(int, input().split())
    tree[s].append(g)
    tree[g].append(s)

for i in range(1, N+1):
    tree[i].sort()

# DFS
dfs_order = []
visited = [False] * (N+1)

def dfs(v):
    visited[v] = True
    dfs_order.append(v)
    for nxt in tree[v]:
        if not visited[nxt]:
            dfs(nxt)
dfs(V)
print(*dfs_order)


# BFS
def bfs(s):
    visited = [False] * (N+1)
    q = deque([s])
    visited[s] = True
    bfs_order = []
    while q:
        cur = q.popleft()
        bfs_order.append(cur)
        for nxt in tree[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return bfs_order

bfs_order = bfs(V)
print(*bfs_order)