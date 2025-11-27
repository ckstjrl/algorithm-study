'''
BOJ2638 : 치즈 (G3)

해결 방법 : 
1. 만약에 주변이 0이 2개보다 많으면, plate에서 0으로 만들고, visited에서 돈 만큼 추가하기
재귀로 돌면서 visited에 녹인 치즈를 확인하고 체크하기
visited에서 가장 큰 수가 답
=> 바깥 공기만 녹인다는 생각을 안함
'''
'''
# visited = [[0]*m for _ in range(n)]

# def melt_cheese(r):
#     blank_cnt = 0
#     queue = deque()
#     for i in range(n):
#         for j in range(m):
#             if plate[i][j] == 1:
#                 queue.append((i, j))
#             else:
#                 blank_cnt += 1
#     if blank_cnt == (m*n):
#         return round-1
#     while queue:
#         ti, tj = queue.popleft()
#         cnt = 0
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#             ni, nj = ti + di, tj + dj
#             if 0<=ni<n and 0<=nj<m:
#                 if plate[ni][nj] == 0:
#                     cnt += 1
#         if cnt >= 2:
#             plate[ti][tj] = 0
#             visited[ti][tj] = r
#     melt_cheese(r+1)

# ans = melt_cheese(1)
# print(ans)
'''
'''
2. 녹일 칸만 bfs로 구하기 : 바깥에서부터 0인 칸만 다 visited에 체크하기 (아닌칸은 1로 체크하기) -> 안쪽 공기는 제외하기
plate에서 1인 칸 중에, visited에서 0이 2개인 경우만 plate에서 제거하기

'''

from collections import deque

n, m = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(n)]

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def external_air(si, sj, visited):
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = 1
    while queue:
        ti, tj = queue.popleft()
        for di, dj in dirs:
            ni, nj = ti + di, tj + dj
            if 0 <= ni < n and 0 <= nj < m:
                if not visited[ni][nj] and plate[ni][nj] == 0:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))

def melt_cheese(r):
    while True:
        visited = [[0]*m for _ in range(n)]
        # 가장자리의 0들에서만 BFS 시작
        for i in range(n):
            if plate[i][0] == 0 and not visited[i][0]:
                external_air(i, 0, visited)
            if plate[i][m-1] == 0 and not visited[i][m-1]:
                external_air(i, m-1, visited)
        for j in range(m):
            if plate[0][j] == 0 and not visited[0][j]:
                external_air(0, j, visited)
            if plate[n-1][j] == 0 and not visited[n-1][j]:
                external_air(n-1, j, visited)

        # 이번 라운드에 녹일 치즈 모으기
        melt = []
        for i in range(n):
            for j in range(m):
                if plate[i][j] == 1:
                    cnt = 0
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 1:
                            cnt += 1
                    if cnt >= 2:
                        melt.append((i, j))

        if not melt:
            return r - 1

        for i, j in melt:
            plate[i][j] = 0
        r += 1

ans = melt_cheese(1)
print(ans)
