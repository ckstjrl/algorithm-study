# 1974. 스도쿠 검증 / D2

# 스도쿠 조건 체크하기 위한 함수 
def issudoku(type, x, y):
    if type == 'box':  # 3x3 박스 내에 
        box = [b[y:y+3] for b in board[x:x+3]]
        numbers = [n for inner in box for n in inner]
    elif type == 'row':  # 같은 행에
        numbers = board[x]
    elif type == 'col':  # 같은 열에 
        numbers = [b[y] for b in board]

    if set(numbers) == set(range(1, 10)):  # 1~9 숫자가 겹치지 않게 있는지
        return True
    else:
        return False


T = int(input())

for t in range(T):
    board = [list(map(int, input().split())) for _ in range(9)]
    # 3x3 박스 체크할 때, 좌표 이동을 위한 리스트
    box_coords = [(0, 0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6)]

    result = 0

    for i in range(9):
        # 각 행/열/박스마다 스도쿠 조건 만족하는지 체크
        sudoku_row = issudoku('row', i, 0)
        sudoku_col = issudoku('col', 0, i)
        sudoku_box = issudoku('box', box_coords[i][0], box_coords[i][1])
        # 조건 만족하지 않는 경우 바로 break
        if not sudoku_box or not sudoku_col or not sudoku_row:
            break
    else:
        result = 1

    print(f'#{t+1} {result}')