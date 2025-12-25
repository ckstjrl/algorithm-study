N = int(input())
rcp = [list(map(int, input().split())) for _ in range(2 * N)]


for i in range(N):
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    cnt_4 = 0
    for j in range(rcp[2 * i][0]):
        if rcp[2 * i][j + 1] == 4:
            cnt_4 += 1
        elif rcp[2 * i][j + 1] == 3:
            cnt_3 += 1
        elif rcp[2 * i][j + 1] == 2:
            cnt_2 += 1
        elif rcp[2 * i][j + 1] == 1:
            cnt_1 += 1
    for j in range(rcp[2 * i + 1][0]):
        if rcp[2 * i + 1][j + 1] == 4:
            cnt_4 -= 1
        elif rcp[2 * i + 1][j + 1] == 3:
            cnt_3 -= 1
        elif rcp[2 * i + 1][j + 1] == 2:
            cnt_2 -= 1
        elif rcp[2 * i + 1][j + 1] == 1:
            cnt_1 -= 1
    if cnt_4 != 0:
        if cnt_4 > 0:
            print('A')
        else:
            print('B')
    elif cnt_3 != 0:
        if cnt_3 > 0:
            print('A')
        else:
            print('B')
    elif cnt_2 != 0:
        if cnt_2 > 0:
            print('A')
        else:
            print('B')
    elif cnt_1 != 0:
        if cnt_1 > 0:
            print('A')
        else:
            print('B')
    else:
        print('D')