# 1873 상호의 배틀필드

T = int(input())

direction = {'^':[-1,0], 'v':[1,0], '<':[0,-1], '>':[0,1]}
arrow_key = {'U':'^', 'D':'v', 'L':'<', 'R':'>'}

def find_tank(H,W,field):
    for i in range(H):
        for j in range(W):
            if field[i][j] in direction.keys():
                return i, j
            
for tc in range(1, T+1):
    H, W = map(int, input().split())

    field = []
    for _ in range(H):
        field.append(list(input()))

    N = int(input())

    order_list = list(input())

    x, y = find_tank(H, W, field)
    
    max_range = max(H, W)
    for order in order_list:
        
        if order == 'S':
            heading = field[x][y]
            for i in range(1,max_range):
                if 0 <= x + direction[heading][0]*i < H and 0 <= y + direction[heading][1]*i < W:
                    if field[x + direction[heading][0]*i][y + direction[heading][1]*i] == '*':
                        field[x + direction[heading][0]*i][y + direction[heading][1]*i] = '.'
                        break
                    elif field[x + direction[heading][0]*i][y + direction[heading][1]*i] == '#':
                        break
                else:
                    break
        else: 
            heading = arrow_key[order]
            if 0 <= x + direction[heading][0] < H and 0 <= y + direction[heading][1] < W and field[x + direction[heading][0]][y + direction[heading][1]] == '.':
                field[x][y] = '.'
                x, y = x + direction[heading][0], y + direction[heading][1]
                
            field[x][y] = heading
    
    print(f'#{tc}')
    for i in range(H):
        print(''.join(field[i]))