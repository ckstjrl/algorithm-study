import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, dist_sum):
    global max_dist, max_node
    if max_dist < dist_sum:
        max_dist, max_node = dist_sum, v
    # 연결된 노드 중 가보지 않은 애들 방문
    for nv, dist in adj[v]:
        if visited[nv] == 1:
            continue
        visited[nv] = 1
        dfs(nv, dist_sum+dist)


V = int(input())
# 인접 리스트 생성
adj = [[] for _ in range(V+1)]
for i in range(V):
    # 노드 번호랑 연결된 애들 나눠주기
    vnum, *temp = list(map(int, input().split()))[:-1]
    # 연결된 애들과 거리가 함께 들어와 인덱스 처리
    for i in range(len(temp)//2):
        adj[vnum].append((temp[2*i],temp[2*i+1]))

visited = [0] * (V+1) # visited 배열 선언
max_dist, max_node = 0, 0
start_node = 1 # 아무 노드에서 시작
visited[start_node] = 1
dfs(start_node,0) # 가장 먼 노드를 찾는 1차 탐색

max_dist = 0
visited = [0] * (V+1)
visited[max_node] = 1
dfs(max_node, 0) # 1차 탐색에서 가장 먼 노드를 찾으면 2차 탐색
print(max_dist)