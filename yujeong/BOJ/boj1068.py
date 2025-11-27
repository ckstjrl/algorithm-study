# 1068. 트리

from collections import deque

# 리스트를 탐색하며 입력받은 노드 기준으로 연결된 노드들을 제거하는 함수 dfs()
def dfs(d):
    q = deque([d])
    while q:
        pos = q.popleft()  
        tree[pos] = 'x'         # 제거한 노드라고 표시 
        for i in range(N):
            if tree[i] == pos:  # 이 노드가 다른 노드의 부모인 경우
                q.append(i)     # 그 노드도 스택에 추가 

# tree에서 남은 리프 노드 개수를 카운트하는 함수 count_leaf()
def count_leaf(arr):
    cnt = 0
    for i in range(N):
        # 제거되지 않았고, 다른 노드들의 부모 노드가 아닌 경우 leaf
        if (arr[i] != 'x') and (i not in arr):
            cnt += 1
    return cnt


N = int(input())    # 노드 개수
tree = list(map(int, input().split()))
d = int(input()) # 제거할 노드 번호 

if tree[d] == -1:   # 제거해야 할 노드가 루트 노드이면
    ans = 0         # 무조건 남은 리프 노드 개수는 0
else:
    dfs(d)          # 그 외의 경우 dfs로 탐색하고 남은 리프 노드 카운트 
    ans = count_leaf(tree)
print(ans)
