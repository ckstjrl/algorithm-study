'''
1210. Ladder1 (D4)
'''

T = 10
 
for _ in range(T):
    tc = int(input())
    N = 100
 
    ladder = [list(map(int, input().split())) for _ in range(N)]
 
    # 거꾸로 도착지에서 시작
    i = 99
    x, y = 0, 0
    for j in range(100):
        if ladder[i][j] == 2:   # 도착지 찾기
            x, y = j, i
    ladder[y][x] = 0
 
    while y > 0:
        if 0 <= x-1 < 100 and 0 <= y < 100 and ladder[y][x-1] == 1: # 왼쪽이 1이면 이동 후 0으로 변환
            x = x-1
            ladder[y][x] = 0
 
        if 0 <= x+1 < 100 and 0 <= y < 100 and ladder[y][x+1] == 1: # 오른쪽이 1이면 이동 후 0으로 변환
            x = x+1
            ladder[y][x] = 0
 
        if 0 <= x < 100 and 0 <= y-1 < 100 and ladder[y-1][x] == 1: # 위쪽이 1이면 이동 후 0으로 변환
            y = y-1
            ladder[y][x] = 0
 
    print(f'#{tc} {x}')