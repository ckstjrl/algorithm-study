# BOJ 3085. 사탕 게임 (D2/S2)

n = int(input())
board = [list(input()) for _ in range(n)]

def count_max():
    max_cnt = 1
    # 행 체크
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
    # 열 체크
    for j in range(n):
        cnt = 1
        for i in range(n-1):
            if board[i][j] == board[i+1][j]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
    return max_cnt

ans = 0
# 인접한 칸 교환
for i in range(n):
    for j in range(n):
        # 오른쪽과 교환
        if j+1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            ans = max(ans, count_max())
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        # 아래와 교환
        if i+1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            ans = max(ans, count_max())
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)