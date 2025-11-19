'''boj1167 트리의 지름
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 
트리의 지름을 구하는 프로그램을 작성하시오.

트리가 입력으로 주어진다. 
먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)
둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.

먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 
하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 
예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 
정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 
각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.
'''

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(node):
    global max_distance, visited_cnt
    max_node = 0

    # 최대 거리 갱신하고 노드 정보 갱신
    if max_distance < visited[node]:
        max_distance = visited[node] - 1
        max_node = node

    # 방문처리 V번 하면 끝 모든 노드가 방문
    if visited_cnt == V:
        return max_node
    
    #node로부터 갈 수 있는 노드들 모두 확인
    # 그 중에서 한 곳으로 진행

    for dist, next_node in adj_list[node]:
        #이미 방문한 지점이면 안감
        if visited[next_node]:
            continue
        
        # 방문 처리에 거리정보 넣기
        visited[next_node] = visited[node] + dist
        visited_cnt += 1
        result = dfs(next_node)
        if result != 0:
            max_node = result

    return max_node

V = int(input())
#인접 리스트 선언 
adj_list = [[] for _ in range(V + 1)]

# 인풋 정보 인접리스트에 넣기 
for _ in range(V):
    #info[0] 은 정점번호, 이후 연결된 간선 번호, 거리정보를 반복하다가 -1이 나오면 끝
    info = list(map(int, input().split()))

    i = 1
    while info[i] != -1:
        next_node = info[i]
        distance = info[i + 1]

        # 주어진 정점 번호의 인접리스트에 (거리, 정점번호)를 추가
        adj_list[info[0]].append((distance, next_node))
        i += 2

# 거리를 내림차순으로 정렬 -> 안해도 될 듯
for ad in adj_list:
    ad.sort(reverse=True, key = lambda x:x[0])


visited = [0] * (V + 1)
visited[1] = 1

# V개의 간선이 모두 visited 처리 되면 끝냄
visited_cnt = 1

#최대 거리
max_distance = 0

#임의의 노드(시작점 1로 가정)에서 가장 먼 노드
ans_node = dfs(1)

#초기화
visited = [0] * (V + 1)
visited[ans_node] = 1
visited_cnt = 1
max_distance = 0

#가장 먼 노드에서 가장 먼 노드
dfs(ans_node)


print(max_distance)
