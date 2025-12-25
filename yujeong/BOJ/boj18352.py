# 18352. 특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline

# 도시 s에서부터 BFS로 다른 도시들을 방문하며 최단거리를 기록하는 함수 bfs()
# 최단거리가 정확히 K인 도시들의 리스트를 리턴 
def bfs(s):    
    stack = deque([s])
    k_lst = []
    while stack:
        p = stack.popleft()
        for nxt in road[p]:
            if visited[nxt] == -1:
                visited[nxt] = visited[p] + 1
                if visited[nxt] == K:
                    k_lst.append(nxt)
                stack.append(nxt)
    
    return k_lst

# 도시 개수 N, 도로 개수 M, 거리 K, 출발 도시 X
N, M, K, X = map(int, input().split())

# 도시 간 도로를 나타내는 인접 리스트 
road = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    road[a].append(b)

visited = [-1] * (N+1)      # 방문 여부와 최단 거리를 기록하는 리스트 visited
visited[X] = 0

ans_lst = bfs(X)            # 시작 노드 X에서부터 탐색

if ans_lst:                 # 거리가 정확히 K인 도시들이 있으면 오름차순으로 출력
    ans_lst.sort()
    print(*ans_lst, sep='\n')
else:                       # 아니면 -1 출력 
    print(-1)
