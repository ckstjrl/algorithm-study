# swea 2806. N-Queen / D3

def putNqueens(x):
    global board, N, cnt
    
    if x == N: # 마지막 열까지 도달했고 Nqueens 조건 만족
        cnt += 1
        return
    
    for y in range(N):
        board[x] = y
        if isNqueens(x):
                putNqueens(x+1) # 다음 열에 놓으러

def isNqueens(x): # Nqueens  조건 만족하는지 체크
    for i in range(x):
        if board[i] == board[x]: # 세로에 있음 
             return False 
        if (board[i] - board[x] == x - i) or (board[x] - board[i] == x - i): # 대각선에 있음
             return False
    print(board)
    return True
        

T = int(input())

for t in range(T):
    N = int(input())
    board = [-1] * N
    cnt = 0
    result = putNqueens(0)

    print(f'#{t+1} {cnt}')
    