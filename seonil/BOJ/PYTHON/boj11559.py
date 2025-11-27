"""
BOJ11559. Puyo Puyo

[문제]
뿌요뿌요의 룰은 다음과 같다.
필드에 여러 가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.
뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.
뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.
아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.
터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.
남규는 최근 뿌요뿌요 게임에 푹 빠졌다. 이 게임은 1:1로 붙는 대전게임이라 잘 쌓는 것도 중요하지만, 상대방이 터뜨린다면 연쇄가 몇 번이 될지 바로 파악할 수 있는 능력도 필요하다.
하지만 아직 실력이 부족하여 남규는 자기 필드에만 신경 쓰기 바쁘다. 상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산하여 남규를 도와주자!

[입력]
총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.
이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.
R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.
입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다. 즉, 뿌요 아래에 빈 칸이 있는 경우는 없다.

[출력]
현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

# 상하좌우 델타 배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 시작 좌표(sy, sx)에서 같은 색(color)의 뿌요가 상하좌우로 얼마나 연결되었는지 BFS로 탐색하고, 4개 이상이면 터뜨리는 함수
def puyo_boom(sy, sx, color):

    # BFS 준비
    q = deque([(sy, sx)])
    visited[sy][sx] = True

    cnt = 1 # BFS로 탐색한 뿌요들을 count
    backup = [] # BFS로 탐색한 뿌요들이 4개 미만일 경우 복구하기 위해 좌표 저장

    # BFS
    while q:
        y, x = q.popleft()
        if cnt < 4: # 탐색한 뿌요가 4개 미만인 경우
            backup.append((y, x))   # backup에 현재 좌표를 저장
        enemy_field_info[y][x] = '.'    # 일단 터뜨린다(cnt < 4면 나중에 복구)

        for dir in range(4):    # 상하좌우 4방향 탐색
            ny, nx = y + dy[dir], x + dx[dir]
            if 0<=ny<12 and 0<=nx<6 and not visited[ny][nx] and enemy_field_info[ny][nx] == color:  # 범위 안이고, 방문하지 않았고, 같은 색 뿌요면 enqueue
                cnt += 1
                visited[ny][nx] = True
                q.append((ny, nx))

    if cnt < 4: # BFS 끝난 후 탐색한 뿌요 개수가 4개 미만이면
        # backup 내의 좌표들을 꺼내서 필드를 복구
        for i in range(len(backup)):
            by, bx = backup[i]
            enemy_field_info[by][bx] = color
        return False    # 터뜨리지 못했으므로 False 반환
    else:
        return True # 터뜨리기 성공했으므로 True 반환

# main
enemy_field_info = [list(input().strip()) for _ in range(12)]   # 적 필드 정보 입력 받기
cnt_chain_reaction = 0  # 총 연쇄 작용이 일어난 횟수를 저장
while True:

    # 1. 뿌요 그룹 터뜨리기
    visited = [[False] * 6 for _ in range(12)]  # 방문 체크 배열
    boomExists = False  # 이번 턴에서 뿌요가 터졌는지 여부를 저장
    for i in range(12): # 전체 필드를 돌면서
        for j in range(6):
            if not visited[i][j] and enemy_field_info[i][j] != '.': # 검사 동안 방문한 적 없고, 빈 칸이 아니면
                if puyo_boom(i, j, enemy_field_info[i][j]): # BFS로 뿌요 그룹 탐색 후 4개 이상이면 터뜨린다!
                    boomExists = True   # 한 번이라도 터지면 True

    # 이번 턴에 터진 뿌요가 없다면, 종료
    if not boomExists:
        break

    # 이번 턴에 뿌요가 터졌다면, 연쇄 작용이 일어난 횟수 +1
    cnt_chain_reaction += 1

    # 2. 각 열마다 중력의 영향 적용하기
    for col in range(6):    # 각 열마다
        
        # 빈 칸은 버리고 남은 뿌요들만 추출
        blocks = [enemy_field_info[row][col] for row in range(12) if enemy_field_info[row][col] != '.']

        # 인덱스를 이용해 밑에서부터 채우기
        for i in range(12):
            if i < len(blocks): # 블록 수만큼 맨 아래부터 채우기
                enemy_field_info[11 - i][col] = blocks[len(blocks) - 1 - i]
            else:   # 블록 수만큼 다 채웠으면 나머지는 '.' 처리
                enemy_field_info[11 - i][col] = '.'

# 12 * 6 뿌요뿌요 필드 정보 출력
# for col in range(12):
#     row = enemy_field_info[col]
#     print(row)

# 결과 반환
print(cnt_chain_reaction)