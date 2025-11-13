import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
friend = [[] for _ in range(N+1)]
for _ in range(M):  # 친구 리스트
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

def kevin(start):  # 함수(시작점)
    visited = [0] * (N + 1)
    visited[start] = 1  # 시작점 방문기록
    q = deque()
    q.append((start,0))  # q에 append
    while q:  # bfs
        user, cnt = q.popleft()
        for x in friend[user]:  # 친구면 방문기록(거리)
            if visited[x] == 0:
                visited[x] = cnt + 1
                q.append((x, cnt + 1))  # 친구의 친구 append(거리+1)
    ans = sum(visited) - 1  # 본인 제외
    return ans

min_v = float('inf')
ans = 0
for i in range(1, N+1):  # 최솟값인 사람 번호 출력
    v = kevin(i)
    if v < min_v:
        min_v = v
        ans = i
print(ans)
