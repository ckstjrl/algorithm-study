# 파리퇴치 3 / D2
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    di_t = [1, 0, -1, 0]
    dj_t = [0, 1, 0, -1]
    di_x = [1, 1, -1, -1]
    dj_x = [1, -1, 1, -1]
    kill_list = []
    for i in range(N):
        for j in range(N):
            kill_t = fly[i][j]
            kill_x = fly[i][j]
            for a in range(4):
                for c in range(1, M):
                    if 0 <= i+di_t[a]*c < N and 0 <= j+dj_t[a]*c < N:
                        kill_t += fly[i+di_t[a]*c][j+dj_t[a]*c]
                    if 0 <= i + di_x[a] * c < N and 0 <= j + dj_x[a] * c < N:
                        kill_x += fly[i + di_x[a] * c][j + dj_x[a] * c]
            kill_list.append(kill_t)
            kill_list.append(kill_x)

    max_k = 0
    for k in kill_list:
        if max_k < k:
            max_k = k
    print(f'#{tc} {max_k}')