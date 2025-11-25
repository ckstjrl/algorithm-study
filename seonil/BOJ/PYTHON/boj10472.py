"""
BOJ10472. 십자뒤집기

[문제]
당신에게 3x3 크기의 보드가 주어진다. 각각의 칸은 처음에 흰색 혹은 검은색이다.
만약 당신이 어떤 칸을 클릭한다면 당신이 클릭한 칸과 그 칸에 인접한 동서남북 네 칸이 (존재한다면) 검은색에서 흰색으로, 혹은 흰색에서 검은색으로 변할 것이다.
당신은 모든 칸이 흰색인 3x3 보드를 입력으로 주어지는 보드의 형태로 바꾸려고 한다. 보드를 회전시킬수는 없다.
(Figure D.1: 예제 입력)

[입력]
첫 줄에는 테스트 케이스의 숫자 P(0 < P ≤ 50)이 주어진다.
각각의 테스트 케이스에 대해서 세 줄에 걸쳐 한 줄에 세 글자씩이 입력으로 들어온다. "*"은 검은색을 뜻하며 "."은 흰색을 뜻한다.

[출력]
각각의 테스트 케이스에 대해서 흰 보드를 입력에 주어진 보드로 바꾸는 데 필요한 최소 클릭의 횟수를 구하여라.
"""

import sys
from collections import deque
import copy
input = lambda: sys.stdin.readline().rstrip()

# 상하좌우 방향 델타 벡터
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 셀 타입 변환용 딕셔너리
cell_types = {
    0: '.',
    1: '*',
}

# (y, x) 위치를 클릭했을 때 십자 모양으로 칸 색상을 '흰색 ↔ 검은색'으로 뒤집는 함수
def cross_toggle(bd, y, x):
    # 클릭한 칸 자체를 토글
    if bd[y][x] == '.':
        bd[y][x] = '*'
    else:
        bd[y][x] = '.'
    
    # 인접한 4방향 칸들도 각각 독립적으로 토글
    for dir in range(4):
        ny, nx = y + dy[dir], x + dx[dir]
        if 0 <= ny < 3 and 0 <= nx < 3:
            if bd[ny][nx] == '.':
                bd[ny][nx] = '*'
            else:
                bd[ny][nx] = '.'

# 리스트는 set에 넣을 수 없으므로 보드를 튜플로 저장하기 위한 함수
def board_to_tuple(bd):
    return tuple(tuple(row) for row in bd)

# 상태 그래프를 BFS로 탐색하여 최소 클릭 횟수를 구하는 함수
def bfs(target):

    # 흰색 3 * 3 보드부터 시작
    start = [['.'] * 3 for _ in range(3)]
    start_t = board_to_tuple(start)
    target_t = board_to_tuple(target)

    # 이미 목표 보드가 모두 흰색이면 최소 클릭 횟수는 0
    if start_t == target_t:
        return 0

    # BFS 준비
    q = deque([(start, 0)])
    visited = {start_t} # set 형태로 visited 설정

    # BFS 시작
    while q:
        cur_bd, dist = q.popleft()

        # 3 * 3의 모든 칸을 눌러보기
        for y in range(3):
            for x in range(3):

                # 현재 board를 복사한 후 (y, x) 클릭한 상태를 다음 board로 설정
                nxt_bd = copy.deepcopy(cur_bd)
                cross_toggle(nxt_bd, y, x)

                nxt_t = board_to_tuple(nxt_bd)

                # 다음 board가 아직 방문하지 않은 보드 상태라면,
                if nxt_t not in visited:
                    # 다음 board가 목표 보드라면 정답 반환
                    if nxt_t == target_t:
                        return dist + 1
                    # 다음 board를 방문 체크하고 큐에 추가
                    visited.add(nxt_t)
                    q.append((nxt_bd, dist + 1))

    return -1  # 도달 실패 시 -1 반환

# main
P = int(input())    # 테스트 케이스 개수
for _ in range(1, P + 1):   # 각 테스트 케이스마다:
    target = [list(input().strip()) for _ in range(3)]  # 3 * 3 목표 보드 입력 받기
    ans = bfs(target)   # bfs를 통해 상태 그래프 탐색하며 최소 클릭 횟수 구하여 ans에 저장
    print(ans)  # 정답 출력
