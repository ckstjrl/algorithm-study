'''
# [Silver II] 트리의 부모 찾기 - 11725 

[문제 링크](https://www.acmicpc.net/problem/11725) 

### 성능 요약

메모리: 62220 KB, 시간: 2916 ms

### 분류

그래프 이론, 그래프 탐색, 트리, 너비 우선 탐색, 깊이 우선 탐색

### 제출 일자

2025년 9월 1일 20:01:46

### 문제 설명

<p>루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.</p>

### 입력 

첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.</p>

### 출력 

첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.</p>
'''

from collections import deque
N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1) :
    p, c = map(int, input().split()) 
    graph[p].append(c)
    graph[c].append(p)

# 부모/자식 배열
parent = [0] * (N+1)
child = [[] for _ in range(N+1)]

# BFS 
q = deque([1])
visited = [0] * (N+1) 
visited[1] = 1
while q :
    cur = q.popleft()
    for next in graph[cur] :
        if not visited[next] :
            parent[next] = cur
            child[cur].append(next)
            visited[next] = 1
            q.append(next)

for i in range(2, N+1):
    print(parent[i])
