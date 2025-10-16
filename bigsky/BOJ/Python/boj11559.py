# BOJ11559(D3): Puyo Puyo
# 1. 4개 이상 같은 색이 모여있으면 .으로 바꾸기
# 2. 아래로 떨어뜨리기
# 3. 1, 2반복 -> 4개 이상 같은 색이 모여있는 경우가 없다면 출력 후 종료
from collections import deque
import sys

arr = [list(sys.stdin.readline().rstrip()) for _ in range(12)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(r, c, color, visited):
    q = deque([(r, c)])
    visited[r][c] = True
    puyo_group = [(r, c)] # 연결된 뿌요들의 좌표 저장

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < 12 and 0 <= nc < 6 and not visited[nr][nc] and arr[nr][nc] == color:
                visited[nr][nc] = True
                q.append((nr, nc))
                puyo_group.append((nr, nc))
    
    return puyo_group

def pop_puyo():
    has_popped = False  # 현재 턴에 터짐 여부
    visited = [[False] * 6 for _ in range(12)]

    for r in range(12):
        for c in range(6):
            if arr[r][c] != '.' and not visited[r][c]:
                puyo_group = bfs(r, c, arr[r][c], visited)
                if len(puyo_group) >= 4:
                    has_popped = True
                    for pr, pc in puyo_group:
                        arr[pr][pc] = '.'
    
    return has_popped

def gravity():
    for c in range(6):
        q = deque()
        for r in range(11, -1, -1):
            if arr[r][c] != '.':
                q.append(arr[r][c])
        for r in range(12):
            arr[r][c] = '.'
        row = 11
        while q:
            arr[row][c] = q.popleft()
            row -= 1

# Main -----------------------------
combo = 0
while True:
    if pop_puyo():
        combo += 1
        gravity()
    else:
        break

print(combo)

