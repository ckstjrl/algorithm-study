# 1167. 트리의 지름

import sys
input = sys.stdin.readline

# start 노드(입력으로 주어진 노드)에서 트리를 DFS로 탐색하며, 
# satrt 노드로부터 가장 먼 거리를 가진 노드의 번호(인덱스)와 그때의 거리를 반환하는 함수 dfs()
def dfs(start):
    visited = [-1] * V
    stack = [(start, 0)]    # 스택에 노드 번호와 간선의 거리를 함께 저장 
    visited[start] = 0      # 출발지에선 누적거리 0
    while stack:
        pos, dist = stack.pop()
        for nxt, c in tree[pos]:                    # 간선으로 연결된 다음 노드에 대해 
            if visited[nxt] == -1:                  # 아직 탐색한 적 없는 노드면
                visited[nxt] = dist + c             # 그 노드까지 이동하는 누적거리 갱신 
                stack.append((nxt, visited[nxt]))   # 스택에 추가

    return visited.index(max(visited)), max(visited)


V = int(input())
tree = [[] for _ in range(V)]
# --------------
# 1차 시도: 간선 정보를 이차원 배열에 저장
# 메모리 초과 발생: 최악의 경우 V가 100,000 
# => 연결되어있지 않은 노드들이 많기 때문에 메모리가 과하게 낭비될 수밖에 없음
# 해결: 인접 리스트 구성 

for i in range(V):
    arr = list(map(int, input().split()))
    j = 1
    while arr[j] != -1:
        # 각 줄의 첫 번째 숫자가 노드 번호, 그 다음은 (연결된 노드 번호, 거리) 쌍 
        tree[arr[0]-1].append((arr[j]-1, arr[j+1]))
        j += 2

end_node, max_dist = dfs(0)

# --------------
# 2차 시도: dfs(0) 한번 실행 -> 여기서 구한 max(visited) 출력
# 근데 생각해보면 첫 노드 (0번)이 끝단(루트 or 지름을 구성하는 리프) 노드일때만 이게 트리의 지름임이 보장되는 것
# 입력이 주어지는 순서가 꼭 트리를 구성하는 순서임이 보장되지 않기 때문에 
# DFS 한번으로는 트리의 지름을 구할 수 없음
# 트리의 지름에 대해 알아본 결과... 트리의 지름의 성질을 생각해보면
# 한 번 DFS했을 때의 누적 최대 거리를 가진 점은 트리의 지름을 구성하는 두 점 중 한 점일 수밖에 없음
# 해결: 이 점에서부터 다시 DFS해서 최대 거리를 구하면 이게 최종 트리의 지름

_, final_dist = dfs(end_node)
print(final_dist)