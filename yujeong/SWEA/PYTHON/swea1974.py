# 1974. 스도쿠 검증 / D2

def issudoku(type, x, y):
    if type == 'box':
        box = [b[y:y+3] for b in board[x:x+3]]
        numbers = [n for inner in box for n in inner]
    elif type == 'row':
        numbers = board[x]
    elif type == 'col':
        numbers = [b[y] for b in board]

    if set(numbers) == set(range(1, 10)):
        return True
    else:
        return False


T = int(input())

for t in range(T):
    board = [list(map(int, input().split())) for _ in range(9)]
    box_coords = [(0, 0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6)]

    result = 0

    for i in range(9):
        sudoku_row = issudoku('row', i, 0)
        sudoku_col = issudoku('col', 0, i)
        sudoku_box = issudoku('box', box_coords[i][0], box_coords[i][1])
        if not sudoku_box or not sudoku_col or not sudoku_row:
            break
    else:
        result = 1

    print(f'#{t+1} {result}')