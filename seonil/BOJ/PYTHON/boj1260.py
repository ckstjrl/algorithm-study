"""
BOJ1260. DFS와 BFS

[문제]
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

[입력]
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

[출력]
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
"""
import sys
from collections import deque
input = sys.stdin.readline

# 깊이 우선 탐색(DFS) 함수
def dfs(V):
    visited = [False] * (N + 1)
    stack = [V]                  # DFS는 스택을 이용 → 시작 정점 V를 먼저 넣어둠
    path = []

    while stack:                 # 스택이 빌 때까지 반복
        t = stack.pop()          # 스택 pop
        if visited[t]:           # 이미 방문한 정점이면 건너뜀
            continue
        visited[t] = True        # 방문 표시
        path.append(t)           # 방문 순서에 추가

        # 인접 리스트에서 연결된 정점들을 스택에 추가
        for w in adj_lst[t]:
            stack.append(w)

    return path                  # DFS 방문 순서 반환


# 너비 우선 탐색(BFS) 함수
def bfs(V):
    visited = [-1] * (N + 1)
    q = deque([V])               # BFS는 큐를 이용 → 시작 정점 V를 큐에 넣음
    visited[V] = 0               # 시작 정점 방문 처리 (거리 = 0)
    path = []

    while q:                        # 큐가 빌 때까지 반복
        t = q.popleft()             # 큐의 맨 앞 원소 dequeue
        path.append(t)              # 방문 순서에 추가
        for w in adj_lst[t]:        # 인접 리스트에서 연결된 정점들 w에 대하여
            if visited[w] == -1:    # 아직 방문하지 않은 정점이라면 큐에 enqueue하고 거리 기록
                q.append(w)
                visited[w] = visited[t] + 1

    return path                  # BFS 방문 순서 반환


# main
N, M, V = map(int, input().split())    # N = 정점 개수, M = 간선 개수, V = 시작 정점
adj_lst = [[] for _ in range(N + 1)]   # 인접 리스트 초기화 (정점 번호는 1부터 사용)

# 간선 입력 받아 인접 리스트에 저장 (양방향)
for _ in range(M):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

# DFS에서 작은 정점 번호부터 탐색하기 위해 각 인접 리스트를 내림차순 정렬
for i in range(N):
    adj_lst[i + 1].sort(reverse=True)

dfs_path = dfs(V)   # DFS 수행
print(" ".join(map(str, dfs_path))) # 방문 순서 출력

# BFS에서 작은 정점 번호부터 탐색하기 위해 각 인접 리스트를 오름차순 정렬
for i in range(N):
    adj_lst[i + 1].sort()

bfs_path = bfs(V)   # BFS 수행
print(" ".join(map(str, bfs_path))) # 방문 순서 출력