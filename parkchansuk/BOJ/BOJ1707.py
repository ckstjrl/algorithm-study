# BOJ 1707. 이분 그래프 / D3
'''
문제
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다.
각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다.
각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.
이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데,
각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다.

출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.
'''
import sys
from collections import deque

def bfs(start): # 이분 그래프 확인 BFS
    q = deque([start])
    visited[start] = 1 # 시작은 방문 1이라고 표시
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if visited[nxt] == 0: # 방문 기록이 없다면
                q.append(nxt)
                visited[nxt] = visited[now] % 2 + 1 # now 가 방문 1이라면 nxt는 방문 2 / now가 2이면 nxt는 1
            else:
                if visited[nxt] == visited[now]: # 방문한 기록이 있다면 now와 nxt의 동일 여부 판단
                    return False # 동일하다면 False 리턴
    return True # 아무 문제 없으면 True 리턴

T = int(sys.stdin.readline().strip())
for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = 'YES'
    for s in range(1, V+1): # 모든 정점을 확인하기 위함
        if visited[s] == 0:
            if not bfs(s): # BFS 결과가 False라면 NO 출력
                ans = 'NO'
                break
    print(ans)
    
    
'''
각 노드에 두가지 색을 칠한다 생각하면
이분 그래프는 서로 연결된 경우 서로 색이 다른 노드로 이루어진 그래프를 뜻함
bfs를 사용하여 visited에 1, 2를 입력하면서 확인 절차를 밟음
끝까지 탐색했는데 연결된 같은 색의 노드가 없다면 YES
있다면 NO 출력
1 - 2
3 - 4
와 같이 서로 연결되지 않은 그래프의 경우 BFS만 사용하면 판단이 불가능하므로
for s in range(1, V+1):
    if visited[s] == 0:
        if not bfs(s):
            ans = 'NO'
            break
문을 사용하여 판단
'''