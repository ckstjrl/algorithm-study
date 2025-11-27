# BOJ1167: 트리의 지름
import sys
from collections import deque


def bfs(node):
    distances = [-1] * (V + 1)
    q = deque([node])
    distances[node] = 0

    max_dist = 0
    farthest_node = node

    while q:
        c_node = q.popleft()

        for neighbor, dist in tree[c_node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[c_node] + dist
                q.append(neighbor)

                if distances[neighbor] > max_dist:
                    max_dist = distances[neighbor]
                    farthest_node = neighbor

    return farthest_node, max_dist


input = lambda: sys.stdin.readline().rstrip()
V = int(input())
tree = [[] for _ in range(V + 1)]

for _ in range(V):
    info = list(map(int, input().split()))
    node = info[0]
    idx = 1
    while info[idx] != -1:
        neighbor = info[idx]
        dist = info[idx + 1]
        tree[node].append((neighbor, dist)) # 트리에 (연결노드, 거리)를 기록해놓는다.
        idx += 2

# 임의의 노드에서 가장 멀리 떨어진 노드를 찾는다.
s_node = 1
farthest_node, _ = bfs(s_node)

# 가장 먼 노드에서 가장 먼 노드까지의 거리를 계산한다.
_, diameter = bfs(farthest_node)

print(diameter)