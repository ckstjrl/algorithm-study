"""
BOJ14503 - 로봇청소기

문제 정의
1. 0-based N x M 배열
2. 청소기의 작동 방식
  1) 청소안된 칸은 청소한다
  2) 인접 4칸 중 청소되지 않은 칸이 없으면 
  -> 방향 유지한 상태로 if 가능 후진 후 1번 else 멈춤
  3) 인접 칸이 청소 안되어있으면
  -> 반시계 회전 -> 앞이 청소 안되어있으면 전진 -> 다시 반복

3. 시작시 방향은 북 남 동 서 순서이지만 문제 시작 후 방향 설정은 반시계방향으로만 작동




"""


def check(i,j):
    if 0 <= i < N and 0 <= j < M:
        return True
    else:
        return False


def clean(i, j, d):
    cnt = 0
    while True:
        # 1. 현재 칸 청소
        if cleaned[i][j] == 0:
            cleaned[i][j] = 1
            cnt += 1
        

        # 2. 청소할 인접칸 탐색
        flag = False
        for _ in range(4):
            d = (d+3) % 4
            ni, nj = i+di[d], j+dj[d]
            if check(ni,nj) and maps[ni][nj] == 0 and cleaned[ni][nj] == 0:
                i, j = ni, nj 
                flag = True
                break
        if flag:
            continue
        
        # 3. 후진 ㄱㄱ

        back = (d+2) % 4
        ni, nj = i+di[back], j+dj[back]
        if check(ni,nj) and maps[ni][nj] == 0:
            i, j = ni, nj
        else:
            break
    return cnt

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
# 북 동 남 서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
cleaned = [[0] * M for _ in range(N)]
ans = clean(r, c, d)
print(ans)

