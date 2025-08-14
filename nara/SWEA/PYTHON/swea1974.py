T = int(input())
standard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for test_case in range(1, T + 1):
    sudoku = [list(input().split()) for _ in range(9)]
    error = 1 # 0일 경우 error
     
    # 행/열 검증
    for j in range(9):
        tmp_list_col = list()
        tmp_list_row = list()
        for i in range(9):
            tmp_list_col.append(sudoku[j][i])
            tmp_list_row.append(sudoku[i][j])
        tmp_list_col.sort()
        tmp_list_row.sort()
        if tmp_list_col == standard and tmp_list_row == standard:
            continue
        else:
            error = 0
     
    # 격자 검증
    for i in range(3):
        for j in range(3):
            tmp_list = list()
            x, y = 3*i+1, 3*j+1
            tmp_list.append(sudoku[x][y])
            for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                tmp_list.append(sudoku[x + dx][y + dy])
            tmp_list.sort()
            if tmp_list != standard:
                error = 0
 
    print(f"#{test_case} {error}")