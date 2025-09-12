# BOJ 16236 : 아기상어
from collections import deque
import sys

def find_babyShark():
    # 아기상어의 위치를 반환
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return i, j


def find_fish(shark_i, shark_j, shark_size):
    # 최단 거리 계산
    q = deque([(shark_i, shark_j, 0)])  # (열, 행, 이동거리)
    visited = [[0] * N for _ in range(N)]  # 방문여부 표시
    visited[shark_i][shark_j] = 0

    fish_candidates = []
    min_distance = N**2

    while q:
        si, sj, distance = q.popleft()
        
        if distance > min_distance:
            continue

        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = si + di, sj + dj
            if (0 <= ni < N) and (0 <= nj < N) and arr[ni][nj] <= shark_size and not visited[ni][nj]:
                visited[ni][nj] = 1
                if 0 < arr[ni][nj] < shark_size:
                    min_distance = distance + 1
                    fish_candidates.append((min_distance, ni, nj))
                
                q.append((ni, nj, distance + 1))
    
    if fish_candidates:
        fish_candidates.sort()
        return fish_candidates[0]
    else:
        return None, None, None


# Main--------------------------------------------------------------------------
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# 초기 상어 크기, 먹은 물고기수, 총 시간
shark_size = 2
eating_count = 0
time = 0

# 아기 상어 위치 찾기
shark_i, shark_j = find_babyShark()

# 더 이상 먹을 수 있는 물고기가 없을 때까지 반복
while True:
    min_distance, ni, nj = find_fish(shark_i, shark_j, shark_size)

    if min_distance is None:
        break

    arr[ni][nj] = 0
    arr[shark_i][shark_j] = 0
    shark_i, shark_j = ni, nj


    time += min_distance
    eating_count += 1

    if eating_count == shark_size:
        shark_size += 1
        eating_count = 0

print(time)