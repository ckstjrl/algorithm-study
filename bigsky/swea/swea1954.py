T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    
    # 방향키
    # (0,1):오른쪽으로 / (1,0):아래로 / (0,-1):왼쪽으로 / (-1,0):위로
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 초기 위치, 초기 방향 설정
    x, y = 0, 0
    direction = 0

    # N^2만큼의 숫자를 arr[x][y]에 넣을 것
    for num in range(1, N ** 2 + 1):
        arr[x][y] = num

        # 방향대로 숫자가 채워지도록 함
        next_x = x + dx[direction]
        next_y = y + dy[direction]

        # 다음 x 또는 y가 0과 N 사이에 오지 않거나,
        # 다음 자리가 0이 아니라면(이미 숫자가 채워져 있다면)
        # 방향 전환
        if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N or arr[next_x][next_y]:
            direction = (direction + 1) % 4
            next_x = x + dx[direction]
            next_y = y + dy[direction]
        
        x, y = next_x, next_y

    print('#'+str(tc))
    for row in arr:
        print(*row)
