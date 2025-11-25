"""
BOJ1303. 전쟁 - 전투

[문제]
전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다.
그러나 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다.
문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.
N명이 뭉쳐있을 때는 N^2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가?
단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

[입력]
첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다.
그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다.
모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다. 당신의 병사와 적국의 병사는 한 명 이상 존재한다.

[출력]
첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.
"""

from collections import deque

import sys
input = lambda: sys.stdin.readline().rstrip()

# 상하좌우 델타 배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# BFS로 그룹의 power level을 측정한 후 team별로 총합을 누적하는 함수
def check_group_pwlv(sy, sx, team):

    global sum_pwlv

    # BFS 준비
    q = deque([(sy, sx)])
    estimated[sy][sx] = True    # 방문(전투력 검사) 체크 함수
    cnt = 1                     # 현재 그룹에 포함된 인원 수를 저장

    # BFS
    while q:
        cur_y, cur_x = q.popleft()  # 큐에서 BFS 현재 좌표 꺼내기
        for dir in range(4):
            ny, nx = cur_y + dy[dir], cur_x + dx[dir]   # 현재 좌표로부터 이웃한 4방향의 다음 좌표 탐색

            # 만약 다음 좌표가 범위 내부이고, 검사 아직 안했고, 우리 팀이면
            if 0<=ny<M and 0<=nx<N and not estimated[ny][nx] and battleground[ny][nx] == team:
                q.append((ny, nx))          # 큐에 추가
                cnt += 1                    # 현재 그룹 인원수 count
                estimated[ny][nx] = True    # 방문(전투력 검사) 체크
    
    # BFS 종료 후 그룹의 power level을 팀별 전투력 합계에 누적
    if team == 'W':                 # 흰색 팀(우리팀)이면
        sum_pwlv[0] += cnt ** 2     # cnt^2을 전투력으로 계산하여 우리팀 합계에 누적
    else:                           # 파란 팀(적팀)이면
        sum_pwlv[1] += cnt ** 2     # cnt^2을 전투력으로 계산하여 적팀 합계에 누적


# main
N, M = map(int, input().split())    # 전쟁터의 가로 크기 N, 세로 크기 M
battleground = [list(input().strip()) for _ in range(M)]    # 전쟁터 정보 입력 받기

estimated = [[False] * N for _ in range(M)] # 방문(전투력 검사) 체크 함수를 전역으로 관리
sum_pwlv = [0, 0]   # power level 합계[우리팀 합계, 적팀 합계]를 [0, 0]으로 초기화

# 전쟁터의 모든 병사들을 순회
for y in range(M):
    for x in range(N):
        if not estimated[y][x]: # 만약 검사 안 한 병사라면
            check_group_pwlv(y, x, battleground[y][x])  # 그 병사가 속한 그룹을 전부 BFS로 검사하기

# power level 합계 결과 출력
print(" ".join(map(str, sum_pwlv)))
