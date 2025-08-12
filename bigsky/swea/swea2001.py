T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 입력값을 그대로 2차원 배열로 만들기
    fly_map = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0  # 가장 많이 죽은 파리
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            curr_kill = 0
            for k in range(M):
                for l in range(M):
                    curr_kill += fly_map[i + k][j + l]
            max_kill = max(max_kill, curr_kill)

    print(f'#{tc} {max_kill}')