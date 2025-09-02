from collections import deque
import sys
input = sys.stdin.readline
N = int(input().strip())
K = int(input().strip())
adj = [[] for _ in range(N+1)]  # 빈 인접 리스트 선언
for _ in range(K):  # node 개수만큼 인풋 받기
    a, b = map(int, input().split())
    adj[a].append(b)    # 양 방향 그래프 선언
    adj[b].append(a)
q = deque([1])  # 문제의 특성상 시작점은 1
visited = [0] * (N+1)   # 방문 여부 표시를 위한 arr 선언
visited[1] = 1  # 시작점은 방문처리
while q:    # 큐가 있으면
    cur = q.popleft()
    for i in adj[cur]:  # 인접 리스트 값
        if visited[i] == 0:     # 방문한 적이 없다면
            visited[i] = 1  # 방문처리
            q.append(i) # 방문 후 인접 정점을 찾기 위해 큐에 넣기
print(sum(visited)-1)   # 시작을 1로 처리해서 전체 방문한 곳 - 1
