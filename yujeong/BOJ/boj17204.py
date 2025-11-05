# 17204. 죽음의 게임
from collections import deque

N, K = map(int, input().split())    # 참여하는 사람의 수, 보성이의 번호
order = [int(input()) for _ in range(N)]    # 각 사람들이 지목하는 사람

# start(0번)에서부터 이어진 간선을 따라 탐색하며 보성이(K번)에 도착하면 걸린 턴 수 리턴
# 탐색 완료했는데 보성이(K번)에 도착하지 못하면 -1 리턴 
def bfs(start):
    q = deque([start])
    visited = [False] * N   # 각 사람에 도착하기 위해 필요한 턴 수 저장할 배열
    visited[start] = 0
    while q:
        curr = q.popleft()
        target = order[curr]
        if not visited[target]:
            visited[target] = visited[curr] + 1
            if target == K:     # 보성이에게 도착; 여기까지 걸린 턴 수 리턴 
                return visited[target]
            q.append(target)

    return -1   # 탐색 완료했는데 보성이에게 걸릴 방법이 없음; -1 리턴

ans = bfs(0)
print(ans)
