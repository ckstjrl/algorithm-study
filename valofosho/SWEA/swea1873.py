"""
문제 로직 정의
1. maps = H*W 2차원 배열
2. 입력된 커맨드를 순서대로 실행
3. check_movable()
    움직일 수 있는지 여부를 확인하는 함수
    #, * - 가 있으면 갈 수 없다
    만약에 움직이려면
    가려는 방향을 먼저 확인해서 maps배열의 끝을 나가지 않는지 확인
    가려는 방향이 물, 벽, 강철벽이면 가려는 방향이 담긴 마크를 현 위치에 담기


"""
# 이동할 위치가 범위 내에 있는지 확인
def check(i,j,H,W):
    if 0<=i<H and 0<=j<W:
        return True
    else:
        return False


def shoot(i,j,H,W):
    di = [-1, 1, 0, 0]
    dj = [0, 0,-1, 1]
    mark = ['^', 'v', '<', '>']
    idx = mark.index(maps[i][j])
    while True:
        for c in range(1, max(H,W)):
            ni, nj = i+di[idx]*c, j+dj[idx]*c
            # 포탄으로 맞춘 경우
            if check(ni,nj,H,W) and maps[ni][nj] == '*':
                maps[ni][nj] = '.'
                return i, j
            # 포탄으로 강철 벽 때린 경우
            elif check(ni,nj,H,W) and maps[ni][nj] == '#':
                return i,j
            # 물, 땅 등 건너는 경우
            elif check(ni,nj,H,W):
                continue
            else:
                return i, j 
    # return i,j

# 이동 함수
def move(i,j,H,W,cmd):
    di = [-1, 1, 0, 0]
    dj = [0, 0,-1, 1]
    # 순서대로 상 하 좌 우 이동
    mark = ['^', 'v', '<', '>']
    if cmd == 'U':
        maps[i][j] = mark[0]
        ni, nj = i+di[0], j+dj[0]
        # 맵 내에서 이동 가능한 지 확인
        if check(ni,nj,H,W) and maps[ni][nj] not in ['#', '*', '-']:
            maps[i][j] = '.'
            maps[ni][nj] = mark[0]
            i, j = ni, nj
        else:
            maps[i][j] = mark[0]
    elif cmd == 'D':
        maps[i][j] = mark[1]
        ni, nj = i+di[1], j+dj[1]
        if check(ni,nj,H,W) and maps[ni][nj] not in ['#', '*', '-']:
            maps[i][j] = '.'
            maps[ni][nj] = mark[1]
            i, j = ni, nj
        else:
            maps[i][j] = mark[1]
    elif cmd == 'L':
        maps[i][j] = mark[2]
        ni, nj = i+di[2], j+dj[2]
        if check(ni,nj,H,W) and maps[ni][nj] not in ['#', '*', '-']:
            maps[i][j] = '.'
            maps[ni][nj] = mark[2]
            i, j = ni, nj
        else:
            maps[i][j] = mark[2]
    elif cmd == 'R':
        maps[i][j] = mark[3]
        ni, nj = i+di[3], j+dj[3]
        if check(ni,nj,H,W) and maps[ni][nj] not in ['#', '*', '-']:
            maps[i][j] = '.'
            maps[ni][nj] = mark[3]
            i, j = ni, nj
        else:
            maps[i][j] = mark[3]
    return i,j
T = int(input())
for test_case in range(1, T+1):
    H, W = map(int, input().split())
    maps =[list(input()) for _ in range(H)]
    N = int(input())
    cmds = list(input())
    found = False
    for i in range(H):
        for j in range(W):
            if maps[i][j] in ['^', 'v', '<', '>']:
                found = True
                break
        if found:
            break
    # 커멘드 입력이 S로 주어지면 shoot 함수 실행
    for cmd in cmds:
        if cmd == 'S':
            i, j = shoot(i, j, H, W)
        # 커멘드 입력이 S가 아니면 이동 함수 실행
        else:
            i, j = move(i, j, H, W, cmd)
    ans = '\n'.join(''.join(arr) for arr in maps)
    print(f"#{test_case} {ans}")
