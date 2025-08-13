t = int(input())

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

for tc in range(1, t+1):
    n, m = map(int, input().split())

    board = [[0]*n for _ in range(n)]
    board[n//2-1][n//2-1] = 2
    board[n//2-1][n//2] = 1
    board[n//2][n//2-1] = 1
    board[n//2][n//2] = 2

    for _ in range(m):
        x, y, color = map(int, input().split())
        board[y-1][x-1] = color

        for dd in range(8):
            idx = 1
            flag = 0
            while True:
                if not 0 <= y-1+di[dd]*idx <= n-1 or not 0 <= x-1+dj[dd]*idx <= n-1:
                    break
                if board[y-1+di[dd]*idx][x-1+dj[dd]*idx] == 0:
                    flag = 1
                    break
                if board[y-1+di[dd]*idx][x-1+dj[dd]*idx] == color:
                    flag = 1                   
                    for k in range(1, idx):
                        if board[y-1+di[dd]*k][x-1+dj[dd]*k] != 0:
                            board[y-1+di[dd]*k][x-1+dj[dd]*k] = color
                    break
                idx += 1
            if flag:
                continue

    cnt_b = 0
    cnt_w = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt_b += 1
            elif board[i][j] == 2:
                cnt_w += 1

    print(f"#{tc} {cnt_b} {cnt_w}")