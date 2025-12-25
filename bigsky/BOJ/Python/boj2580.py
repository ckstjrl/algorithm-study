# BOJ2580(D3): 스도쿠
import sys

# 스도쿠 판은 가로*세로 9칸
SIZE = 9

# 스도쿠 입력받기
sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(SIZE)]

# 채워야 할 칸의 좌표 리스트
blank_coor = [(i, j) for i in range(SIZE) for j in range(SIZE) if sudoku[i][j] == 0]

def check(y, x, check_num):
    BOX_SIZE = 3
    for i in range(SIZE):
        if check_num == sudoku[i][x] or check_num == sudoku[y][i]:
            return False
    for i in range(BOX_SIZE):
        for j in range(BOX_SIZE):
            if check_num == sudoku[y//BOX_SIZE * BOX_SIZE + i][x//BOX_SIZE * BOX_SIZE + j]:
                return False
    return True

def dfs(n):
    if n == len(blank_coor):
        for i in sudoku:
            print(*i)
        exit()
    for check_num in range(1, 10):
        y, x = blank_coor[n]
        if check(y, x, check_num):
            sudoku[y][x] = check_num
            dfs(n+1)
            sudoku[y][x] = 0

dfs(0)