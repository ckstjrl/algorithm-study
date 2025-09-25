"""
BOJ1987. 알파벳

[문제]
세로 R칸, 가로 칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

[입력]
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

[출력]
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
"""
import sys
sys.setrecursionlimit(10000)   # 파이썬 재귀 깊이 제한을 늘려줌 (최대 400칸까지 이동할 수 있으므로 안전하게 설정)
input = lambda: sys.stdin.readline().rstrip()

# 상하좌우 방향 이동을 위한 델타 배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x, cnt, visited): # (y, x): 현재 좌표, cnt: 지금까지 지나온 칸 수, visited: 지금까지 지나온 알파벳 집합

    global max_cnt
    # 최대 이동 칸 수 갱신
    max_cnt = max(max_cnt, cnt)

    # 알파벳은 총 26개밖에 없으므로, 최대 26이면 더 탐색할 필요 없음 (가지치기)
    if max_cnt == 26:
        return

    # 상하좌우 탐색
    for dir in range(4):
        ny, nx = y + dy[dir], x + dx[dir]
        # 보드 범위 내에 있고, 아직 방문하지 않은 알파벳이라면
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in visited:
            # 알파벳 추가
            visited.add(board[ny][nx])
            # 다음 칸으로 이동
            dfs(ny, nx, cnt + 1, visited)
            # 백트래킹: 다른 경로 탐색을 위해 다시 제거
            visited.discard(board[ny][nx])

# main
R, C = map(int, input().split())                  # 보드 크기 입력
board = [list(input().strip()) for _ in range(R)] # 보드 정보 입력 (알파벳 저장)

max_cnt = 0                                       # 최대 칸 수 기록 변수
dfs(0, 0, 1, {board[0][0]})            # (0,0)에서 시작, 시작 알파벳을 visited에 추가
print(max_cnt)                                    # 최종 결과 출력
