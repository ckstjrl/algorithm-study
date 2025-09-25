# 1707. 이분 그래프
import sys
input = sys.stdin.readline
from collections import deque

# dfs로 그래프를 탐색하며 이분 그래프인지 판별해 리턴
def dfs(start):
    s = deque([start])
    check[start] = True     # 그래프의 각 노드를 True/False로 이분 

    while s:
        cur = s.pop()
        flag = check[cur]       # cur 노드의 True/False 값
        for nxt in graph[cur]:          # cur과 간선으로 연결된 노드 nxt에 대해
            if check[nxt] == -1:
                check[nxt] = not(flag)  # 아직 T/F 값 지정 안 된 노드면 정해주기
                s.append(nxt)
            else:
                if check[nxt] == flag:  # cur과 nxt가 같은 T/F 집합에 속하면
                    return False        # 이분 그래프 아님 
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())    # 정점 V개, 간선 E개
    graph = [[] for _ in range(V+1)]    # 인접 리스트로 그래프 나타내기
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    check = [-1] * (V + 1)  # 각 노드의 탐색 여부와 T/F 집합 기록할 리스트
    is_bipartite = True     # 탐색 결과 이 그래프가 이분 그래프인지 여부 

    for i in range(1, V+1): # 1 ~ V번 노드
        if check[i] == -1:  # 아직 탐색하지 않은 노드 있으면 탐색
            if not dfs(i):  
                is_bipartite = False
                break

    print('YES' if is_bipartite else 'NO')