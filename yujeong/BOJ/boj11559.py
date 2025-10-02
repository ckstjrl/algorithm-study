# 11559. Puyo Puyo
from collections import deque

# 상하좌우로 같은 색 뿌요 4개가 연결되었는지 찾아 좌표들을 반환하는 함수 bfs()
def bfs(pos):
    q = deque([pos])
    cnt = 0
    color = field[pos[0]][pos[1]]
    pop_pos = []
    while q:
        px, py = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = px+dx, py+dy
            if 0<=nx<12 and 0<=ny<6 and field[nx][ny] == color and not visited[nx][ny]:
                cnt += 1
                q.append((nx, ny))
                visited[nx][ny] = True
                pop_pos.append((nx, ny))
    if cnt >= 4:    # 4개 이상 모여 있음
        return pop_pos
    return False    # 터뜨릴 뿌요 없음 

# 뿌요들이 터진 후 아래로 떨어지게 하는 함수 clean()
def clean():
    for w in range(6):
        puyo = deque()  # 빈칸이 아닌 (아래로 떨어져야 하는) 뿌요들 차례로 담기
        for h in range(11, -1, -1): # 아래에서부터 위로 
            if field[h][w] != '.':
                puyo.append(field[h][w])
        for h in range(11, -1, -1):
            if puyo:    # 다시 맨 아래에서부터 뿌요 차례로 넣기
                field[h][w] = puyo.popleft()
            else:       # 넣을 뿌요 없으면 빈칸
                field[h][w] = '.'


field = [list(input()) for _ in range(12)]      # 게임 필드
ans = 0                                         # 뿌요들이 연쇄로 터진 횟수 저장

# while문 1턴 = 1연쇄
while True:
    visited = [[False] * 6 for _ in range(12)]      # 한 턴에 같은 좌표는 한 번만 방문
    clear_lst = deque()                             # 이번 턴에 연쇄로 터뜨릴 뿌요들 좌표
    # 게임 맵 순회하며 같은 색 뿌요 4개 모인 곳 찾기
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and not visited[i][j]:
                pop_lst = bfs((i, j))
                if pop_lst:     # 모인 뿌요들 있으면 터뜨릴 좌표 리스트에 추가 
                    clear_lst += pop_lst

    if not clear_lst:   # 터질 뿌요가 없는 경우; 
        break

    for x, y in clear_lst:  # 터질 뿌요가 있는 경우;
        field[x][y] = '.'   # 터뜨리고 빈칸으로 만들기 

    clean()     # 뿌요들 아래에 빈칸이 있으면 아래로 떨어지게
    ans += 1    # 연쇄 횟수 +1

print(ans)
