import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)

def find(x):
    visited = [0] * (N+1)
    h = 0
    q = deque([x])
    while q:  # BFS
        a = q.popleft()
        if visited[a] == 0:  # 방문 기록 없으면
            h = h + 1  # cnt +1, 방문 기록
            visited[a] = 1
            for b in arr[a]:  # 다음 컴퓨터 q에 append
                q.append(b)
    return h

ans = [0] * (N+1)
for i in range(1, N+1):  # 모든 컴퓨터를 시작점으로 각각 BFS
    ans[i] = find(i)
max_h = max(ans)
ans_2 = []
for i in range(1, N+1):
    if ans[i] == max_h:
        ans_2.append(i)
print(*ans_2)