"""
BOJ14500. 테트로미노

[문제]
폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

* 정사각형은 서로 겹치면 안 된다.
* 도형은 모두 연결되어 있어야 한다.
* 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
* 정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.

아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.
테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

[입력]
첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)
둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

[출력]
첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.
"""
import sys
input = sys.stdin.readline

def inside(y, x, N, M): # 좌표 (y, x)가 종이(N x M) 안에 있는지 확인
    return 0 <= y < N and 0 <= x < M

# DFS를 이용해 테트로미노 모양(4칸짜리) 중 연결된 모양을 탐색하여 합을 구하는 함수
def cal_tetromino_sum_by_dfs(y, x, depth, total):
    global max_tetromino_sum

    # 4칸을 모두 선택했으면 합의 최댓값 갱신
    if depth == 4:
        max_tetromino_sum = max(max_tetromino_sum, total)
        return

    # 상, 하, 좌, 우 네 방향으로 이동
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if inside(ny, nx, N, M) and not visited[ny][nx]: # 종이 안쪽에 있고 방문 안했으면
            visited[ny][nx] = True # 방문하고,
            cal_tetromino_sum_by_dfs(ny, nx, depth + 1, total + paper[ny][nx]) # dfs 수행하면서 부분합 저장
            visited[ny][nx] = False   # 백트래킹

# DFS로는 만들 수 없는 T 스핀 모양을 따로 검사하는 함수
# 중심 좌표(y, x)에서 T자 모양이 가능한지 확인 후 합을 계산
def check_T_shape(y, x):

    global max_tetromino_sum
    # 4가지 T자 모양 (ㅗ, ㅜ, ㅓ, ㅏ)
    shapes = [
        [(0, 0), (0, 1), (0, -1), (1, 0)],   # ㅗ 모양
        [(0, 0), (0, 1), (0, -1), (-1, 0)],  # ㅜ 모양
        [(0, 0), (1, 0), (-1, 0), (0, 1)],   # ㅓ 모양
        [(0, 0), (1, 0), (-1, 0), (0, -1)],  # ㅏ 모양
    ]

    for shape in shapes:
        total = 0
        is_tetromino_inside = True
        for dy, dx in shape:
            ny, nx = y + dy, x + dx
            if not inside(ny, nx, N, M):   # 종이를 벗어나면 불가능
                is_tetromino_inside = False
                break
            total += paper[ny][nx]
        if is_tetromino_inside:   # 종이 안에 전부 들어간 경우만 최댓값 갱신
            max_tetromino_sum = max(max_tetromino_sum, total)

# main
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]   # 우, 하, 좌, 상 (DFS 탐색 방향)
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
max_tetromino_sum = 0   # 테트로미노가 놓인 칸에 쓰인 수들의 최댓값 저장
visited = [[False] * M for _ in range(N)]  # 방문 체크 배열

# 모든 칸에서 DFS + T모양 예외 검사를 수행
for i in range(N):
    for j in range(M):
        # DFS 탐색 (T스핀 모양 제외한 모든 테트로미노 탐색 가능)
        visited[i][j] = True
        cal_tetromino_sum_by_dfs(i, j, 1, paper[i][j])
        visited[i][j] = False

        # T스핀 모양 예외 처리
        check_T_shape(i, j)

# 결과 출력
print(max_tetromino_sum)
