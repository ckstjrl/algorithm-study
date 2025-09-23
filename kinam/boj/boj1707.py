'''boj1707 - 이분 그래프
그래프의 정점의 집합을 둘로 분할하여, 
각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.
'''
# 둘로 분할 -> 1, 2로 나눔 
# 한 정점이 1이라고 하면 인접 정점은 2이어야함
# 1 - 2 - 3 - 4 면 1 - 2 - 1 - 2로 나눌 수 있음 1: (1, 3), 2: (2, 4)
# DFS or BFS로 그래프 탐색하면서 visited를 통해 1과 2 정하기
# 사이클이 있는 경우가 애매할듯
# >> 정점이 홀수개인데 사이클이면 안댈듯 1 - 2 - 3 - 4 - 5 - 1 을 생각해봄  

import sys
sys.setrecursionlimit(10000)

T = int(input()) # 테스트 케이스
for t in range(1, T+1):
    V, E = map(int, input().split()) # 정점의 개수 V, 간선의 개수 E
    adj_list = [[] for _ in range((V + 1))]
    visited = [0] * (V + 1)
    ans = 'NO'

    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)



    def dfs(node, odd):
        for i in adj_list[node]:
            if not visited[i]:
                if odd:
                    visited[i] = 2 # 서로 다르게 방문표시해주기
                    dfs(i, False)

                else:
                    visited[i] = 1
                    dfs(i, True)

    # 방문하지 않은 각 정점에 대하여 dfs를 수행한다.
    for v in range(1, V+1):
        if not visited[v]:
            dfs(v, True)


    # for else 구문을 활용하여 인접 리스트가 서로 다르지 않으면 이분 리스트가 아님을 나타낸다
    isbreak = 0
    for i in range(1, V+1):
        for j in adj_list[i]:
            if visited[i] == visited[j]:
                isbreak = 1
                break
        if isbreak == 1:
            break
    else:
        ans = 'YES'

    print(ans)
    