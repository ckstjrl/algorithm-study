def rowcolumn_correct(arr, x, y):
    # 각 좌표의 행/열에 같은 수가 있는지 탐색
    for i in range(9):
        if i != y:
            if arr[x][i] == arr[x][y]:
                return 0
        if i != x:
            if arr[i][y] == arr[x][y]:
                return 0
         
    return 1
 
def room_correct(arr, x, y):
    # 각 좌표의 방 안에 같은 수가 있는지 탐색
    k, l = x // 3, y // 3
    room_nums = []
 
    for i in range(3):
        for j in range(3):
            if i != x % 3 or j != y % 3:
                room_nums.append(arr[k*3 + i][l*3 + j])
    if arr[x][y] in room_nums:
        return 0
     
    return 1
 
T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
 
    flag = 1
 
    for i in range(9):
        for j in range(9):
            if not rowcolumn_correct(arr, i, j) or not room_correct(arr, i, j):
                flag = 0
                break
        if flag == 0:
            break
     
    print(f'#{tc} {flag}')