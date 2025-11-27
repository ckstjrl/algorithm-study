def hide_and_seek(N, K):
    MAX = 100000
    if N >= K:
        return N - K
    visited = [-1] * (MAX + 1) # visited에 '방문 시간'을 기록 (-1은 아직 방문 안 했다는 의미)

    # 시작점 N을 queue에 넣고, 초기 시간 0을 visited[N]에 기록
    q = [N]
    visited[N] = 0

    # pop을 위한 head 포인터 설정
    head = 0

    while head < len(q): # queue가 비어 있지 않으면

        # queue에서 현재 위치 x를 꺼낸다.
        x = q[head]
        head += 1

        # 현재 위치가 목표지점 K이면, visited[x]에 기록된 방문 시간을 반환하고 종료한다.
        if x == K:
            return visited[x]

        # 현재 위치 x가 목표지점 K를 넘겼으면, x-1만 고려한다.
        # x-1이 방문하지 않은 지점이면 queue에 넣고, 방문 시간에 (현재 시간 + 1)을 기록한다.
        if x > K:
            nx = x - 1
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)
            continue

        # 현재 위치 x가 목표지점 K보다 작다면, x - 1, x + 1, x * 2 를 순회한다.
        # 만약 다음 위치가 유효한 지점이고, 방문하지 않았다면, queue에 넣고, 방문 시간에 (현재 시간 + 1)을 기록한다.
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)

N, K = map(int, input().split())
print(hide_and_seek(N, K))

## [error code]
# 오류 원인 예측 : q.pop()는 리스트의 맨 앞을 빼면서 모든 원소를 한 칸씩 당기는 O(n) 연산이라 틀릴 위험이 있다
# def hide_and_seek(N, K):
#     MAX = 100000
#     visited = [-1] * (MAX + 1)  # 방문 시간 기록 (-1은 아직 방문 안 했다는 의미)
#     q = []
#
#     # 시작점을 queue에 넣고, 초기 시간 0을 visited[N]에 기록
#     q.append(N)
#     visited[N] = 0
#
#     while queue: # queue가 비어 있을 때까지
#         x = q.pop() # queue에서 현재 위치를 꺼냄
#
#         if x == K: # 현재 위치가 목표지점이면
#             return visited[x]  # visited[x]에 기록된 방문 시간을 반환하고 종료한다.
#
#         for w in (x-1, x+1, x*2): # 다음 이동 위치 w를 순회
#             if 0 <= w <= MAX and visited[w] == -1: # 만약 다음 위치가 유효한 지점이고, 방문하지 않았다면
#                 if w > K and w != x-1:  # 가지치기: 다음 위치가 목표지점을 넘으면서 동시에 멀어지는 방향으로 이동하는 경우는 제외한다.
#                     continue
#                 q.append(w) # 위 조건을 만족하지 않는 다음 이동 위치들은 queue에 넣는다.
#                 visited[w] = visited[x] + 1 # visited[w]에 (현재 시간 + 1)을 넣는다.
#
# N, K = map(int, input().split())
# print(hide_and_seek(N, K))