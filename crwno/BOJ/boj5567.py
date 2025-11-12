from collections import deque

N = int(input())
M = int(input())

route = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    route[a].append(b)
    route[b].append(a)


visited = [False] * (N + 1)
q = deque([(1, 0)])
visited[1] = True
cnt = 0



while q:
    pnt, d = q.popleft()

    if d >= 2:
        continue
    for n_pnt in route[pnt]:
        if not visited[n_pnt]:
            visited[n_pnt] = True
            cnt += 1
            q.append((n_pnt, d + 1))

print(cnt)