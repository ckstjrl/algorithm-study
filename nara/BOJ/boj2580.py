import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]

zero = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append([i, j])

def check_num (i, j, n):
    if  n in sudoku[i]:
        return False

    for k in range(9):
        if sudoku[k][j] == n:
            return False

    for k in range(i//3*3, i//3*3+3):
        for l in range(j//3*3, j//3*3+3):
            if sudoku[k][l] == n:
                return False
    return True

def solve(state=0):
    if len(zero) == state:
        for i in range(9):
            print(*sudoku[i])
        sys.exit()

    i, j = zero[state]
    for n in range(1, 10):
        if check_num(i, j, n):
            sudoku[i][j] = n
            solve(state+1)
            sudoku[i][j] = 0

solve()