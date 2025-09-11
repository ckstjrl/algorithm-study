N = int(input())
P = list(map(int, input().split()))
a = int(input())
C = {}
for i in range(N):
    C[i] = []
root = -1
for i in range(N):
    if P[i] == -1:
        root = i  # 루트노드
    else:
        C[P[i]].append(i)  # 부모 : [자식] 딕셔너리
cnt = 0
def dfs(node):
    global cnt
    if node == a:  # 삭제할 a부터 탐색x
        return  
    children = []
    for child in C[node]:
        if child != a:  # 삭제할 노드 제외 자식 노드
            children.append(child)
    if not children:  # 자식이 없으면 카운트 + 1
        cnt += 1
        return
    for child in children:  # 자식노드로 재귀
        dfs(child)
dfs(root)
print(cnt)