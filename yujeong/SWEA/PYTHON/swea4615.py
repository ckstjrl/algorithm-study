# 4615. 재미있는 오셀로 게임 / D3

def move(i, j, color):
    global board
    # 움직일 수 있는 뱡향 8가지
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), 
            (-1, 1), (-1, -1), (1, 1), (1, -1)]
    i -= 1
    j -= 1
    board[i][j] = color
    for x, y in dirs:
        arr = []
        for k in range(1, N+1):
            cx, cy = i+x*k, j+y*k
            if 0<=cx<N and 0<=cy<N:         # 유효한 인덱스인지 체크
                if board[cx][cy] == 0:    
                    break                   # 빈 곳이 있으면 그 방향으로 뒤집기 불가능하므로 break
                elif board[cx][cy] != color:  # 다른 색 돌이 있으면 뒤집기 후보 좌표로 기록
                    arr.append((cx, cy))
                else:                       # 같은 색 돌이 있으면 이때까지 기록한 좌표 돌 뒤집기
                    if arr:
                        for dx, dy in arr:
                            board[dx][dy] = color
                    break  # 검흰검흰흰검 이런식일때 한구간만 뒤집는거 
                    

T = int(input())

for t in range(T):
    # 보드 길이 N (4, 6, 8 중 하나)
    # 돌 놓는 횟수 M
    N, M = map(int, input().split())
    # (위치i, 위치j, 돌 색) -- 돌 색이 1이면 흑 2이면 백
    play = [list(map(int, input().split())) for _ in range(M)]

    board = [[0] * N for _ in range(N)] # 보드 

    # 초기 돌 배치
    board[N//2-1][N//2-1], board[N//2][N//2] = 'W', 'W'
    board[N//2-1][N//2], board[N//2][N//2-1] = 'B', 'B'

    for p in play:
        if p[-1] == 1:
            move(p[0], p[1], 'B')
        else:
            move(p[0], p[1], 'W')   
    
    w_cnt, b_cnt = 0, 0
    for row in board:
        for square in row:
            if square == 'W':
                w_cnt += 1
            elif square == 'B':
                b_cnt += 1

    print(f'#{t+1} {b_cnt} {w_cnt}')
