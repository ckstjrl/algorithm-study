# BOJ 1167. 트리의 지름 (D3 /G2)


'''
트리의 지름: 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것
트리의 지름을 구하는 프로그램을 작성하시오.

 "트리에서 임의의 점에서 가장 먼 점은 반드시 지름의 끝점 중 하나"
'''

#-----------------------------------------------2회차 풀이
# 스택으로
import sys

# 대천way
input = lambda: sys.stdin.readline().rstrip()

def dfs(start):
    stack = [(start, 0, -1)]  # (노드, 누적거리, 부모)
    distances = {}
    
    while stack:
        node, dist, parent = stack.pop()
        distances[node] = dist
        
        for next_node, edge_length in graph[node]:
            if next_node != parent:  # 부모로 다시 가지 않기
                stack.append((next_node, dist + edge_length, node))
    
    max_dist = max(distances.values())
    farthest_node = max(distances, key=distances.get)
    return max_dist, farthest_node

N = int(input())

# 각 노드에 연결된 노드 번호와, 그 사이의 거리를 담은 인접 리스트 생성 
graph = [[] for _ in range(N+1)]
for _ in range(N):
    line = list(map(int, input().split()))
    node = line[0]

    i = 1
    while line[i] != -1:    # -1이 나올 때까지
        pair = line[i]
        distance = line[i+1]
        graph[node].append((pair, distance))
        i+=2


# 1번 노드에서 가장 먼 노드 찾기
visited = [0] * (N+1)
_, first = dfs(1)

# 찾은 노드에서 가장 먼 노드 찾기 = 지름
visited = [0] * (N+1)
second, _ = dfs(first)

print(second)

##-----------------------------------------------1회차 풀이
# import sys
#input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(300000)

# def dfs(node):
#     # 현재까지 누적 거리를 들고 다니면서
#     # 연결된 노드들 탐색    
#     visited[node] = 1
#     max_dist = 0
#     farthest_node = node
#     for next_node, edge_length in graph[node]:
#         if visited[next_node] == 0:
#             dist, far_node = dfs(next_node)
#             total_dist = dist + edge_length

#             if total_dist > max_dist:
#                 max_dist = total_dist
#                 farthest_node = far_node

#     return max_dist, farthest_node

# N = int(input())

# # 각 노드에 연결된 노드 번호와, 그 사이의 거리를 담은 인접 리스트 생성 
# graph = [[] for _ in range(N+1)]
# for _ in range(N):
#     line = list(map(int, input().split()))
#     node = line[0]

#     i = 1
#     while line[i] != -1:    # -1이 나올 때까지
#         pair = line[i]
#         distance = line[i+1]
#         graph[node].append((pair, distance))
#         i+=2


# # 1번 노드에서 가장 먼 노드 찾기
# visited = [0] * (N+1)
# _, first = dfs(1)

# # 찾은 노드에서 가장 먼 노드 찾기 = 지름
# visited = [0] * (N+1)
# second, _ = dfs(first)

# print(second)