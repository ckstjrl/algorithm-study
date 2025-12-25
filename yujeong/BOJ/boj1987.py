# 1987. 알파벳
import sys
input = sys.stdin.readline


# 백트래킹으로 보드를 탐색하며 탐색가능한 최대 알파벳 개수를 세는 함수 recur()
def recur(pos, cnt):
    global max_c
    max_c = max(cnt, max_c)
    if max_c == 26:     # 알파벳 개수 26개보다 많이 탐색할 수 없으므로 가지치기
        return
    px, py = pos[0], pos[1]
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = px+dx, py+dy
        if 0<=nx<R and 0<=ny<C:
            c = board[nx][ny]
            if c not in visited:    # 아직 지난 적 없는 알파벳이면 그쪽으로 탐색
                visited.add(c)
                recur((nx, ny), cnt+1)
                visited.remove(c)   # 백트래킹
    return


R, C = map(int, input().split())    # 세로 R, 가로 C
board = [list(input()) for _ in range(R)]
visited = set(board[0][0])          # 탐색한 알파벳을 set으로 기록
max_c = 0                           # 탐색가능한 알파벳 최대 개수
recur((0, 0), 1)

print(max_c)