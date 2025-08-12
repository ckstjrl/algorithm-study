# 1954. 달팽이 숫자 D2
# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
# [제약사항]
# 달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)
# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어진다.
# [출력]
# 각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# 해결 방법 : 일단 좌표로 돌아보자... -> 다시 풀어야 함... (이해는 했으나 재풀이 필요)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    maze = [[0] * N for _ in range(N)] # 빈 격자 만들기

    # 달팽이 시작 설정 (맨 왼쪽 위)
    x, y = 0, 0
    direction = 0 # 시작 방향 : 0 = 오른쪽
    # direction = 1 : 아래
    # direction = 2 : 왼쪽
    # direction = 3 : 위

    dx = [0, 1, 0, -1] # 행 변화량 (다른 행으로 이동)
    dy = [1, 0, -1, 0] # 열 변화량 (다른 열로 이동)

    for i in range(1, N*N + 1): # 1부터 N*N까지 숫자를 하나씩 현재 위치에 넣기
        maze[x][y] = i

        if i == N * N: # 마지막 숫자면 종료
            break
    
        # 다음 위치 계산
        next_x = x + dx[direction]
        next_y = y + dy[direction]

        # 벽에 닿았나 확인하기
        if (next_x < 0 # 위쪽 벽을 넘어감
            or next_x >= N # 아래쪽 벽을 넘어감
            or next_y < 0 # 왼쪽 벽을 넘어감
            or next_y >= N # 오른쪽 벽을 넘어감
            or maze[next_x][next_y] != 0): # 이미 숫자가 있는 칸
            direction = (direction + 1) % 4 # 새로운 방향으로 다시 계산 (시계 방향 회전)
            next_x = x + dx[direction]
            next_y = y + dy[direction]

        x, y = next_x, next_y # 실제로 이동하기

    # 출력
    print(f"#{test_case}")
    for row in maze: # 2차원 배열 출력
        print(' '.join(map(str, row)))