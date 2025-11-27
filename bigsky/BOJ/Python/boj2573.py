# BOJ2573(D3): 빙산
from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def melt():
    dec = [[0] * M for _ in range(N)]  # 올 해 감소량을 따로 저장

    for r in range(N):
        for c in range(M):
            # 빙산이 아닌 부분은 pass
            if arr[r][c] == 0:
                continue
            # 빙산의 경우 주변 바다 수 만큼 높이를 줄인다.
            # 이번 년도 빙산이었던 부분을 고려한다.
            sea = 0
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                    sea += 1
            dec[r][c] = sea
    
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0:
                arr[r][c] = max(0, arr[r][c] - dec[r][c])


def count_ice():
    # 산 수 세기
    visited = [[False] * M for _ in range(N)]
    cnt = 0

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0 or visited[r][c]:
                continue
            cnt += 1
            if cnt >= 2:
                return 2
            q = deque([(r, c)])
            visited[r][c] = True
            while q:
                cr, cc = q.popleft()
                for k in range(4):
                    nr, nc = cr + dr[k], cc + dc[k]
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0 and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True

    return cnt

# Main --------------------------
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

years = 0

while True:
    groups = count_ice()
    if groups == 0:
        print(0)
        break
    if groups >= 2:
        print(years)
        break
    melt()
    years += 1
