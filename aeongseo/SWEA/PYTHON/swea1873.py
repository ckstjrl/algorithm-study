'''
1873. 상호의 배틀필드

전차가 이동을 하려고 할 때, 만약 게임 맵 밖이라면 전차는 당연히 이동하지 않는다.
전차가 포탄을 발사하면, 포탄은 벽돌로 만들어진 벽 또는 강철로 만들어진 벽에 충돌하거나 게임 맵 밖으로 나갈 때까지 직진한다.
만약 포탄이 벽에 부딪히면 포탄은 소멸하고, 부딪힌 벽이 벽돌로 만들어진 벽이라면 이 벽은 파괴되어 칸은 평지가 된다.

초기 게임 맵의 상태와 사용자가 넣을 입력이 순서대로 주어질 때, 모든 입력을 처리하고 나면 게임 맵의 상태가 어떻게 되는지 구하는 프로그램을 작성하라.
'''

T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    acts = list(input())

    for di in range(H):      # 전차 위치 찾기
        for dj in range(W):
            if arr[di][dj] == '^' or arr[di][dj] == 'v' or arr[di][dj] == '<' or arr[di][dj] == '>':
                tank = arr[di][dj]
                i, j = di, dj

    for act in acts:
        # 동작이 U일 때
        if act == 'U':
            tank = '^'
            if 0 <= i-1 <H and arr[i-1][j] == '.':   # 맵을 벗어나지 않고 윗칸이 평지일 때 이동
                arr[i][j] = '.'
                arr[i-1][j] = '^'
                i = i-1
            else: arr[i][j] = '^'

        # 동작이 D일 때
        if act == 'D':
            tank = 'v'
            if 0 <= i+1 <H and arr[i+1][j] == '.':   # 맵을 벗어나지 않고 아랫칸이 평지일 때 이동
                arr[i][j] = '.'
                arr[i+1][j] = 'v'
                i = i+1
            else: arr[i][j] = 'v'

        # 동작이 L일 때
        if act == 'L':
            tank = '<'
            if 0 <= j-1 <W and arr[i][j-1] == '.':   # 맵을 벗어나지 않고 왼칸이 평지일 때 이동
                arr[i][j] = '.'
                arr[i][j-1] = '<'
                j = j-1 
            else: arr[i][j] = '<'

        # 동작이 R일 때
        if act == 'R':
            tank = '>'
            if 0 <= j+1 <W and arr[i][j+1] == '.':   # 맵을 벗어나지 않고 오른칸이 평지일 때 이동
                arr[i][j] = '.'
                arr[i][j+1] = '>'
                j = j+1
            else: arr[i][j] = '>'

        # 동작이 S일 때
        if act == 'S':
            if tank == '^':                                     # 위로 포탄 발사
                for d in range(i, -1, -1):
                    if arr[d][j] == '#':                        # 강철벽이면 소멸
                        break
                    elif arr[d][j] == '*':                      # 벽돌벽이면 파괴 후 소멸
                        arr[d][j] = '.'
                        break
            if tank == 'v':                                     # 아래로 포탄 발사
                for d in range(i, H):
                    if arr[d][j] == '#':                        # 강철벽이면 소멸
                        break
                    elif arr[d][j] == '*':                      # 벽돌벽이면 파괴 후 소멸
                        arr[d][j] = '.'
                        break
            if tank == '<':                                     # 왼쪽으로 포탄 발사
                for d in range(j, -1, -1):
                    if arr[i][d] == '#':                        # 강철벽이면 소멸
                        break
                    elif arr[i][d] == '*':                      # 벽돌벽이면 파괴 후 소멸
                        arr[i][d] = '.'
                        break
            if tank == '>':                                     # 오른쪽으로 포탄 발사
                for d in range(j, W):
                    if arr[i][d] == '#':                        # 강철벽이면 소멸
                        break
                    elif arr[i][d] == '*':                      # 벽돌벽이면 파괴 후 소멸
                        arr[i][d] = '.'
                        break
    print(f'#{tc}', end=' ')
    for x in arr:
        print(''.join(x))