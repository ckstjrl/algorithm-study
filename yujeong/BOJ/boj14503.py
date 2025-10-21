# 14503. 로봇 청소기

import sys
input = sys.stdin.readline

# 청소
def clean(pos, d):
    global cnt
    px, py = pos[0], pos[1]

    # 현재 칸이 청소되지 않은 칸이면 청소
    if room[px][py] == 0:
        room[px][py] = 2    # 청소한 칸으로 표시
        cnt += 1            # 청소한 칸 수 +1

    # 주변 4칸 중 청소되지 않은 빈 칸 있는지 탐색
    for _ in range(4):
        d = (d + 3) % 4                     # 반시계 방향 90도 돌리기
        dx, dy = dirs[d][0], dirs[d][1]
        nx, ny = px + dx, py + dy
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:   # 청소 안 된 빈 칸이면
            clean((nx, ny), d)              # 1칸 전진해 청소(1번으로)
            return

    # 주변 4칸 중 청소되지 않은 빈 칸 없음
    dx, dy = dirs[d][0], dirs[d][1]     
    bx, by = px-dx, py-dy
    if 0<=bx<N and 0<=by<M and room[bx][by] != 1:   # 후진할 수 있으면
        clean((bx, by), d)                          # 후진 (하고 1번으로)
    return


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # 북 동 남 서 순서로 방향
start_pos = (r, c)      # 시작 좌표
cnt = 0                 # 청소한 칸 수

clean(start_pos, d)     # (현재 위치 좌표), 현재 바라보고 있는 방향 

print(cnt)
