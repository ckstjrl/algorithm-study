T = int(input())
for test_case in range(1, 1+T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    w_count = 0
    for i in range(N):
        for j in range(N-K+1):   # 가로 방향 자리의 수 찾기
            if j == 0 and arr[i][:K] == [1]*K and arr[i][K] == 0:
                w_count = w_count + 1
            if j == N-K and arr[i][N-K:N+1] == [1]*K and arr[i][N-K-1] == 0:
                w_count = w_count + 1
            if 1 <= j <= N - K -1 and arr[i][j:j+K] == [1]*K and arr[i][j-1] == 0 and arr[i][j+K] == 0:
                w_count = w_count + 1
 
    arr_1 = arr
    for i in range(N):
        for j in range(N):   # 가로세로 뒤집기
            if i > j:
                arr_1[i][j], arr_1[j][i] = arr_1[j][i], arr_1[i][j]
 
    for i in range(N):
        for j in range(N - K + 1):   # 세로 방향 자리의 수 찾기
            if j == 0 and arr_1[i][:K] == [1] * K and arr_1[i][K] == 0:
                w_count = w_count + 1
            if j == N - K and arr_1[i][N - K:N + 1] == [1] * K and arr_1[i][N - K - 1] == 0:
                w_count = w_count + 1
            if 1 <= j <= N - K -1 and arr[i][j:j + K] == [1] * K and arr_1[i][j - 1] == 0 and arr_1[i][j + K] == 0:
                w_count = w_count + 1
 
    print(f'#{test_case} {w_count}')