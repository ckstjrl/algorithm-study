# 좌표 (x, y)가 게임 맵 범위 안에 있는지 확인하는 함수
def inside(x, y, H, W):
    if 0 <= x < W and 0 <= y < H:
        return True
    else:
        return False

T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1, T+1):

    H, W = map(int, input().split())  # 게임 맵의 높이(H)와 너비(W) 입력
    game_map = [list(input()) for _ in range(H)]  # H줄에 걸쳐 맵 상태 입력
    N = int(input())  # 명령어 개수 입력
    command = list(input())  # 명령어 문자열을 리스트로 변환

    cur_tank = ['^', 'v', '<', '>']  # 전차가 바라보는 방향 기호 모음

    # 방향 벡터 (dx, dy) — 위, 아래, 왼쪽, 오른쪽
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 현재 전차 위치 찾기
    for i in range(H):
        for j in range(W):
            if game_map[i][j] in cur_tank:  # 전차 기호가 있는 좌표
                x = j  # 전차의 x좌표 (열)
                y = i  # 전차의 y좌표 (행)

    # 명령어 하나씩 처리
    for action in command:

        # 위로 이동
        if action == 'U':
            game_map[y][x] = '^'  # 전차 방향 변경
            dir = 0  # 위쪽 인덱스
            nx, ny = x + dx[dir], y + dy[dir]  # 이동하려는 좌표
            if inside(nx, ny, H, W):  # 맵 안인지 확인
                if game_map[ny][nx] == '.':  # 평지라면 이동
                    game_map[y][x], game_map[ny][nx] = game_map[ny][nx], game_map[y][x]
                    x, y = nx, ny  # 전차 위치 갱신

        # 아래로 이동
        if action == 'D':
            game_map[y][x] = 'v'
            dir = 1
            nx, ny = x + dx[dir], y + dy[dir]
            if inside(nx, ny, H, W):
                if game_map[ny][nx] == '.':
                    game_map[y][x], game_map[ny][nx] = game_map[ny][nx], game_map[y][x]
                    x, y = nx, ny

        # 왼쪽으로 이동
        if action == 'L': 
            game_map[y][x] = '<'
            dir = 2
            nx, ny = x + dx[dir], y + dy[dir]
            if inside(nx, ny, H, W):
                if game_map[ny][nx] == '.':
                    game_map[y][x], game_map[ny][nx] = game_map[ny][nx], game_map[y][x]
                    x, y = nx, ny

        # 오른쪽으로 이동
        if action == 'R':
            game_map[y][x] = '>'
            dir = 3
            nx, ny = x + dx[dir], y + dy[dir]
            if inside(nx, ny, H, W):
                if game_map[ny][nx] == '.':
                    game_map[y][x], game_map[ny][nx] = game_map[ny][nx], game_map[y][x]
                    x, y = nx, ny

        # 포탄 발사
        if action == 'S':
            cur_x, cur_y = x, y  # 현재 전차 좌표 저장
            # 전차의 현재 방향 찾기
            for k in range(4):
                if game_map[y][x] == cur_tank[k]:
                    dir = k
            nx, ny = x + dx[dir], y + dy[dir]  # 포탄의 다음 좌표

            # 포탄 진행 시뮬레이션
            while inside(nx, ny, H, W):
                if game_map[ny][nx] == '#':  # 강철 벽이면 아무 일도 안 하고 종료
                    break
                elif game_map[ny][nx] == '*':  # 벽돌 벽이면 파괴 후 종료
                    game_map[ny][nx] = '.'
                    break
                else:  # 평지 또는 물이면 계속 전진
                    nx, ny = nx + dx[dir], ny + dy[dir]

            # 전차 좌표 복구
            x, y = cur_x, cur_y

    # 결과 출력
    print(f'#{test_case} {"".join(game_map[0])}')  # 첫 번째 줄 출력
    for i in range(1, H):  # 나머지 줄 출력
        print("".join(game_map[i]))
