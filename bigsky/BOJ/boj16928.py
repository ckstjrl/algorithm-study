# BOJ16928(D3) : 뱀과 사다리 게임
from collections import deque

N, M = map(int, input().split())
path = [0] * 101
for _ in range(N + M):
    a, b = map(int, input().split())
    path[a] = b
visited = [-1] * 101

q = deque([1])  # (위치, 횟수)
visited[1] = 0

while q:
    pos = q.popleft()
    if pos == 100:
        break

    for i in range(1, 7):
        if pos + i <= 100:
            n_pos = pos + i
            if path[n_pos]:
                n_pos = path[n_pos]
            if visited[n_pos] == -1:
                visited[n_pos] = visited[pos] + 1
                q.append(n_pos)

print(visited[100])