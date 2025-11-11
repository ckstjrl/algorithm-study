# BOJ11725. 트리의 부모 찾기

# import sys
# # 재귀 깊이 제한
# sys.setrecursionlimit(10**6)

# # dfs 
# def dfs(s):
#     for i in adj_list[s]:
#         if not visited[i]: # 아직 노드를 방문하지 않았다면
#             visited[i] = s # i의 부모는 s
#             dfs(i)


def dfs():
    stack = [1] 
    while stack: 
        s = stack.pop() 
        for i in adj_list[s]:
            if not visited[i]: # 아직 노드를 방문하지 않았다면
                visited[i] = s # i의 부모는 s
                stack.append(i) # 자식 노드 i를 다음 탐색을 위해 스택에 추가

V = int(input())
E = V - 1

# 인접 리스트 만들기
adj_list = [[] for _ in range(V+1)]

for i in range(E):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visited = [0] * (V + 1)

dfs()

for i in range(2, V+1):
    print(visited[i])