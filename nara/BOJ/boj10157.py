import sys
input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
else:
    arr = [[0] * C for _ in range(R)]
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dir = 0
    x, y = 0, 0
    seat = 1
    arr[y][x] = seat

    while seat < K:
        nx = x + dirs[dir][0]
        ny = y + dirs[dir][1]

        if 0 <= nx < C and 0 <= ny < R and arr[ny][nx] == 0:
            x = nx
            y = ny
            seat += 1
            arr[y][x] = seat
        else:
            dir = (dir + 1) % 4
    print(x+1, y+1)