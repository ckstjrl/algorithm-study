# arr 내 idx에서 벗어나지 않는지
def check(x,y,N):
    if 0<=x<N and 0<=y<N:
        return True
    else:
        return False
    
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    # 2차원 배열 기준 우, 하, 좌, 상 이동 반복
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # N * N 2차원 배열 생성
    arr = [[0] * N for _ in range(N)]
    # 초기 좌표 설정
    x, y = 0, 0
    dir = 0
    # 값을 바로 대입하기 위해 range(1, N**2 + 1)
    for i in range(1, N**2 + 1):
        arr[x][y] = i
        # 새로운 좌표가 arr내에 있고, 이미 지나가지 않은 즉, 초기 0값이라면 진행
        if check(x+dx[dir],y+dy[dir],N) and arr[x+dx[dir]][y+dy[dir]] == 0:
            x, y = x+dx[dir], y+dy[dir]
        # 그렇지 않다면 방향 전환을 위해 (dir+1)%4 -> 4방향을 반복적으로 순회
        else:
            dir = (dir+1)%4
            x, y = x+dx[dir], y+dy[dir]
    print(f"#{test_case}")
    # 각 행의 값들을 문자열로 변환하여 출력
    for r in arr:
        print(" ".join(map(str, r)))
