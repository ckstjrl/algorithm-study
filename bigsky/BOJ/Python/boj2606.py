# BOJ2606: 바이러스
# 트리구조를 통해 문제를 풀어야하는데...
import sys
from collections import deque

def bfs(t, s):
    q = deque([s])
    visited = [0] * (N + 1)
    visited[s] = 1

    cnt = 0

    while q:
        c_node = q.popleft()
        for n_node in tree[c_node]:
            if not visited[n_node]:
                visited[n_node] = 1
                q.append(n_node)
                cnt += 1
    
    return cnt

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

tree = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

print(bfs(tree, 1))