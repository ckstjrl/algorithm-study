'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''



N, M, V = map(int, input().split())  # N = 정점 수, M은 간선 수, V는 시작 정점.

graph = []
for _ in range(N + 1):  # 1번부터 N번까지 쓰기 위해 N+1 크기로 만듦.
    graph.append([])  # 각 정점의 이웃 목록을 저장.

for _ in range(M):  # M개의 간선을 입력받음.
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 여기까지 간선 정보를 만들었음.

# DFS를 위한 방문 배열과 결과 리스트.
visited_dfs = [False] * (N + 1)  # DFS에서 방문 여부를 기록.
dfs_order = []  # DFS 방문 순서를 저장.

def dfs(u):
    visited_dfs[u] = True 
    dfs_order.append(u)
    # 작은 번호부터 방문하기 위해 매번 정렬하자.
    for v in sorted(graph[u]): 
        if not visited_dfs[v]:
            dfs(v)

visited_bfs = [False] * (N + 1) 
bfs_order = []  

def bfs(start):
    q = [start]  
    visited_bfs[start] = True  
    while q:  
        cur = q.pop(0) 
        bfs_order.append(cur) 
        # 작은 번호부터 방문하기 위해 매번 정렬해보자.
        for nxt in sorted(graph[cur]):  
            if not visited_bfs[nxt]: 
                visited_bfs[nxt] = True
                q.append(nxt)

dfs(V) 
bfs(V) 



print(*dfs_order)  
print(*bfs_order) 