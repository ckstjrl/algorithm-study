"""
문제 정의
1. 양방향 친구 관계 트리가 주어진다.
2. 사람은 두 종류 얼리어답터 or 일반인
3. 아이디어 수용 조건은 본인이 일반인이라면 모든 친구 관계가 얼리어답터여야 함
4. 친구 관계 트리가 주어졌을 때 모든 개인이 새로운 아이디어 수용을 위해 필요한 최소 얼리 어답터의 수

로직 생각 중
1. 리프 노드에서부터 시작한다면, 리프노드들은 우선 0으로 처리, 리프의 부모들은 채우기
2. 리프의 부모들의 친구들은 0 처리, 각각 visited 처리하면서 방문하지 않은 정점 방문
3. 해당 정점은 0으로 내비두고 다시 부모 노드 찾아가기

로직 정리
1. 부모만 존재하는 즉 adj[x] 의 길이가 1인 x들은 leaf로 leafs에 추가
2. leafs를 순회하면서 leaf의 부모를 얼리어답터라 생각
3. 부모의 친구들과의 연쇄를 끊어서 부모의 친구들이 하나의 이웃만을 갖게되면 leaf로 치부하고 추가
4. leafs에서 순회 중 부모가 존재하면 cnt += 1
"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

leafs = deque()
for i in range(N+1):
    if len(adj[i]) == 1: # 리프는 부모만 존재, 자식 X
        leafs.append(i)
cnt = 0
while leafs:
    leaf = leafs.popleft()
    # 친구나 부모가 이미 손절
    if len(adj[leaf]) == 0:
        continue
    # 리프는 부모만 adj[leaf]에 있음
    parent = adj[leaf][0]
    # 부모가 얼리어답터가 아니면 얼리어답터로!
    cnt += 1
    # 부모님 친구들
    friends = adj[parent][:]
    for friend in friends:
        # 부모님이랑 친구들 손절
        adj[friend].remove(parent)
        adj[parent].remove(friend)
        # 친구가 손절당하고 혼자 남으면 leaf로
        if len(adj[friend]) == 1:
            leafs.append(friend)
print(cnt)