'''
BOJ16236 : 아기 상어 (G3)

해결 방법 : 
1. 아기 상어가 있는 좌표를 저장해놓고, 0으로 변경하기
2. bfs로 작거나 같은 경우에만 q로 갈 수 있는 칸 표시
3. 가장 위, 왼쪽에 있는 같은 거리의 칸을 후보[0]로 해서 가기

'''

from collections import deque
import sys

input = sys.stdin.readline

n = int(input().strip())
board = []
shark_r = shark_c = 0

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 9:
            shark_r, shark_c = i, j
            row[j] = 0
    board.append(row)

size = 2
eat_cnt = 0
time = 0

def bfs(sr, sc, size):
    q = deque()
    q.append((sr, sc))
    visited = [[0] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    visited[sr][sc] = 1

    candidates = []

    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    while q:
        ti, tj = q.popleft()

        for di, dj in directions:
            ni = ti + di
            nj = tj + dj

            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if board[ni][nj] > size:
                    continue

                visited[ni][nj] = 1
                dist[ni][nj] = dist[ti][tj] + 1
                q.append((ni, nj))

                if 0 < board[ni][nj] < size:
                    candidates.append((dist[ni][nj], ni, nj))

    if not candidates:
        return None

    candidates.sort()
    return candidates[0]

while True:
    result = bfs(shark_r, shark_c, size)

    if result is None:
        break

    d, fish_r, fish_c = result

    time += d
    shark_r, shark_c = fish_r, fish_c

    board[fish_r][fish_c] = 0
    eat_cnt += 1

    if eat_cnt == size:
        size += 1
        eat_cnt = 0

print(time)