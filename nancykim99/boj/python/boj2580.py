'''
BOJ2580 : 스도쿠 (D3 / G4)
'''

'''
해결 방법 : 
1. 스도쿠 구현하기 -> 안 됨
    1) 가로로 제거하기
        a. 일단 돌면서 있는 숫자 하나씩 제거하기
        b. 1~9까지 남은 숫자가 1개인 경우
        c. 남은 숫자를 0에 넣기
    2) 세로로 제거하기
        a~c. 동일
    3) 네모로 제거하기
        a. (2, 9, 3) -> 2, 5, 8인 경우에만 (i, j가)
        b. 사각형, 대각선, 기준점을 다 돌면서 있는 숫자 하나씩 제거하기
        c. 남은 숫자가 1개인 경우
        d. 남은 숫자를 0에 넣기

    def play_sudoku():
        # 가로로 제거하기
        for i in range(9):
            num_list_del = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            cnt_0 = 0
            idx_0 = []
            if '0' in sudoku[i]:
                for j in range(9):
                    if sudoku[i][j] != '0':
                        num_list_del.remove(sudoku[i][j])
                    else:
                        cnt_0 += 1
                        idx_0.append([i, j])
                if cnt_0 == 1:
                    i_0 = idx_0[0][0]
                    j_0 = idx_0[0][1]
                    sudoku[i_0][j_0] = num_list_del[0]

        # 세로로 제거하기
        for i in range(9):
            num_list_del = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            cnt_0 = 0
            idx_0 = []
            for j in range(9):
                if sudoku[j][i] != '0':
                    num_list_del.remove(sudoku[j][i])
                else:
                    cnt_0 += 1
                    idx_0.append([j, i])
            if cnt_0 == 1:
                j_0 = idx_0[0][0]
                i_0 = idx_0[0][1]
                sudoku[j_0][i_0] = num_list_del[0]

        # 네모로 제거하기
        for i in range(1, 9, 3):
            for j in range(1, 9, 3):
                num_list_del = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                cnt_0 = 0
                idx_0 = []
                for ti, tj in [[0,0],[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
                    ni = i + ti
                    nj = j + tj
                    if sudoku[ni][nj] != '0':
                        num_list_del.remove(sudoku[ni][nj])
                    else:
                        cnt_0 += 1
                        idx_0.append([ni, nj])
                if cnt_0 == 1:
                    i_0 = idx_0[0][0]
                    j_0 = idx_0[0][1]
                    sudoku[i_0][j_0] = num_list_del[0]

    play_sudoku()

2. 백트래킹 하기
    1) 새로운 숫자를 0인 곳에 하나씩 넣기
    2) 넣을 때마다 가로줄, 세로줄, 네모를 확인해서 이미 있는지 확인하기
    3) 만약에 새로운 숫자가 이미 있으면 다시 0으로 돌아가서 다음 숫자 넣기
    4) 없으면, 다음 0으로 넘어가기
'''

import sys

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

# 빈칸에 새로운 숫자를 넣어도 괜찮은지 check
def is_valid(num, r, c):
    # 가로줄 check
    for i in range(9):
        if sudoku[r][i] == num:
            return False
    # 세로줄 check
    for i in range(9):
        if sudoku[i][c] == num:
            return False
    # 네모 check
    box_r = (r // 3) * 3
    box_c = (c // 3) * 3
    for i in range(box_r, box_r + 3):
        for j in range(box_c, box_c + 3):
            if sudoku[i][j] == num:
                return False
    # 채우려는 숫자가 가로줄, 세로줄, 네모에 없어서 넣어도 된다면
    return True


def solve_sudoku(idx):
    if idx == len(zeros):
        return True

    row, col = zeros[idx]

    for num in range(1, 10):
        if is_valid(num, row, col):
            sudoku[row][col] = num # 숫자를 넣음

            # 잘 채웠으면 다음 껄로 가기
            if solve_sudoku(idx + 1):
                return True 

            
            sudoku[row][col] = 0

    return False

solve_sudoku(0)

for i in range(9):
    print(*(sudoku[i])) 