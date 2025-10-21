# BOJ14503(D3): 로봇 청소기
import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())  # 방 크기
r, c, d = map(int, input().split())  # 로봇 좌표, d(0북, 1동, 2남, 3서)
room = [list(map(int, input().split())) for _ in range(N)]  # 청소x: 0, 벽: 1

cnt = 0

while True:
    # 청소가 되지 않은 곳이라면 청소처리(3) 후 cnt++
    if room[r][c] == 0:
        room[r][c] = 3
        cnt += 1

    moved = False
    for _ in range(0, 4):
        d = (d + 3) % 4
        nr, nc = r + dr[d], c + dc[d]
        if room[nr][nc] == 0:
            r, c = nr, nc
            moved = True
            break

    if not moved:
        back = (d + 2) % 4
        nr, nc = r + dr[back], c + dc[back]
        if room[nr][nc] == 1:
            print(cnt)
            break
        else:
            r, c = nr, nc
