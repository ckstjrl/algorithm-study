# BOJ 1068. 트리 (D3, G5)

#-----------------------------1회차 풀이
def dfs(node, deleted):
    # 삭제된 노드면 탐색 X
    if deleted[node]:
        return 0
    
    leaf_count = 0
    child_count = 0 
    
    # 자식 탐색
    
    for child in children[node]:
        if not deleted[child]:
            child_count += 1
            leaf_count += dfs(child, deleted)
    
    # 자식이 없으면 리프노드
    if child_count == 0:    
        return 1
    else:
        return leaf_count


def mark_deleted(node, deleted):
    # 현재 노드 삭제 표시
    deleted[node] = 1
    # 모든 자식 노드도 삭제 (재귀)
    for child in children[node]:
        mark_deleted(child, deleted)

N = int(input())
arr = list(map(int, input().split()))
target = int(input())

#트리에서 인접리스트를 타고타고 다 지우기
children = [[] for _ in range(N)]
root = -1

for i in range(N):
    if arr[i] == -1:
        root = i
    else:
        children[arr[i]].append(i)
                
#타겟을 보았을 때 연결된것들을 다 지우고, 연결된 것들에 연결된것들도 다 지우기
deleted = [0] * N
#삭제할 노드와 서브트리 표시
mark_deleted(target, deleted)

#루트가 삭제되면 트리가 없음
if deleted[root]:
    print(0)
else:
    print(dfs(root, deleted))