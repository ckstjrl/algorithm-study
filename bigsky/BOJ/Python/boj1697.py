from collections import deque

def bfs(N, K):
    q = deque([(N, 0)]) # (위치, 시간)
    visited = [0] * 100001
    visited[N] = 1

    while q:
        c_pos, c_time = q.popleft()

        if c_pos == K:
            return c_time
        
        n_moves = [c_pos - 1, c_pos + 1, c_pos * 2]

        for n_pos in n_moves:
            if 0 <= n_pos < 100001 and not visited[n_pos]:
                visited[n_pos] = 1
                q.append((n_pos, c_time + 1))


N, K = map(int, input().split())

if N >= K:
    print(N - K)
else:
    print(bfs(N, K))