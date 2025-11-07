# BOJ1260. DFS와 BFS
from collections import deque 

N, M, V = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)

for i in range(N + 1):
    adj_list[i].sort()

visited_dfs = [False] * (N + 1)
# dfs
def dfs(s):
    print(s, end=' ')
    visited_dfs[s] = True
    for i in adj_list[s]:
        if not visited_dfs[i]:
            dfs(i)

# bfs
def bfs(s):
    visited_bfs = [False] * (N + 1)
    queue = deque([s]) 
    visited_bfs[s] = True 
    while queue:
        t = queue.popleft()
        print(t, end=' ')
        for i in adj_list[t]:
            if not visited_bfs[i]:
                visited_bfs[i] = True 
                queue.append(i)

dfs(V)
print() 
bfs(V)