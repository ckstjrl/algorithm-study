# """
# BOJ1068 - 트리
# 문제 정의:
# 1. 트리의 노드 개수 N
# 2. 0 번 노드 부터 N- 1 번 노드까지 각 노드의 부모가 주어진다
# 3. 부모가 없다면 (루트) -1 이 주어진다.
# 4. 지울 노드의 번호가 주어진다

# 생각 정리
# 1. 리프노드의 정의는 무엇인가
# -> 본인을 부모노드로 가지고 있는 노드가 없다면 그 아이가 곧 리프 노드다
# 그렇다면 어떻게 값을 형성해야 하는가

# """
from collections import deque

N = int(input())
# 인접 리스트 생성
adj = [[] for _ in range(N)]


arr = list(map(int, input().split()))
# idx, value 순서
root = 0
for child, parent in enumerate(arr):
    # 자식의 정보를 저장한 일방향 노드 생성
    if parent == -1:
        root = child
        adj[child].append(-1)
        continue
    adj[parent].append(child)
    adj[child].append(child)
K = int(input())
if K == root:
    print(0)
else:
    q = deque([K])
    while q:
        # 노드 번호 고르기
        cur = q.popleft()
        # 자식 노드 리스트 -> 자기 자신 포함임
        node = adj[cur]
        for n in node:
            if n == cur:
                continue
            q.append(n)
        adj[cur] = []
    cnt = 0
    for i in range(N):
        # 자기 자신 혹은 자식이 있는 노드라면
        if len(adj[i]) >= 1:
            flag = False
            # 자기 자신이라면 넘기고
            for j in adj[i]:
                if j == i:
                    continue
                # 자식이라면 flag = True(리프 아님)
                else:
                    if adj[j]:
                        flag = True
                        break
            if not flag:
                cnt += 1
    print(cnt)
