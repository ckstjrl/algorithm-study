import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(5)]
lst = []
for _ in range(5):
    lst.extend(list(map(int, input().split())))
def find(i):
    for x in range(5):
        for y in range(5):
            if arr[x][y] == i:  # 빙고숫자 찾으면
                arr[x][y] = 0   # 0으로 
                break
def bingo():
    cnt = 0
    cnt_1 = 0   # 대각선카운트 5되면 빙고
    cnt_2 = 0   # 대각선카운트 5되면 빙고
    for i in range(5):
        if arr[i] == [0,0,0,0,0]:  # 가로빙고
            cnt = cnt + 1
        if arr[0][i] == 0 and arr[1][i] == 0 and arr[2][i] == 0 and arr[3][i] == 0 and arr[4][i] == 0:
            cnt = cnt + 1  # 세로빙고
        if arr[i][i] == 0:
            cnt_1 = cnt_1 + 1
        if arr[i][4-i] == 0:
            cnt_2 = cnt_2 + 1
    if cnt_1 == 5:
        cnt = cnt + 1
    if cnt_2 == 5:
        cnt = cnt + 1
    if cnt >= 3:  # 빙고3개 이상이면 1 리턴
        return 1
    
for i in range(len(lst)):
    find(lst[i])
    if bingo() == 1:  # 1리턴이면 몇번째 숫자인지 출력
        print(i+1) 
        break