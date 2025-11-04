import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt_neg_one = 0
cnt_zero = 0
cnt_one = 0

def check(x, y, n):
    start = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != start:
                return False
    return True

def devide(x, y, n):
    global cnt_neg_one, cnt_zero, cnt_one
    if check(x, y, n):
        if arr[x][y] == -1:
            cnt_neg_one += 1
        elif arr[x][y] == 0:
            cnt_zero += 1
        else:
            cnt_one += 1
        return

    size = n // 3
    for i in range(3):
        for j in range(3):
            devide(x + i*size, y + j*size, size)

devide(0, 0, N)

print(cnt_neg_one)
print(cnt_zero)
print(cnt_one)