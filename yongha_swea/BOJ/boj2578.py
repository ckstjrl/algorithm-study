#boj2578 빙고

#가로, 세로 빙고 체크를 위한 함수
def bingo_check():
    global check

    bingo = 0

    for i in range(5):
        bingo_hor = True
        bingo_ver = True
        for j in range(5):
            if check[i][j] != 1:
                bingo_hor = False
            if check[j][i] != 1:
                bingo_ver = False
        if bingo_hor:
            bingo += 1
        if bingo_ver:
            bingo += 1
    return bingo

#점차로 내려가는 대각선, 올라가는 대각선 빙고 확인을 위한 함수
def diag_bingo_check():
    global check
    
    bingo = 0
    diag_down_bingo = True
    diag_up_bingo = True

    for i in range(5):
        if check[i][i] != 1:
            diag_down_bingo = False
        if check[i][4-i] != 1:
            diag_up_bingo = False
    
    if diag_down_bingo:
        bingo += 1
    if diag_up_bingo:
        bingo += 1
    
    return bingo


#각 판에 순서를 받은 배열을 게임판의 형태로 받기
board = [list(map(int, input().split())) for _ in range(5)]

call = [list(map(int, input().split())) for _ in range(5)]
#불리는 순서에 대한 2차원 배열을 편의를 위해 1차원으로 변경하기
call = sum(call, [])

#visited역할을 해줄 빈 배열을 board와 동일한 크기로 만들기
check = [[0] * 5 for _ in range(5)]

#사회자가 말해주는 숫자의 순서 카운팅
count = 0

while call:
    num = call[count]

    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                check[i][j] = 1
    
    count += 1

    #매 숫자마다 빙고 개수 계산을 위한 함수 호출
    bingo = bingo_check() + diag_bingo_check()

    #빙고가 3줄이 된 순간의 부른 숫자의 개수 출력
    if bingo >= 3:
        print(count)
        break
    