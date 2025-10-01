stick = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    cnt = 0
    for j in range(4):
        if stick[i][j] == 0:
            cnt += 1
    if cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D')
    elif cnt == 0:
        print('E')
