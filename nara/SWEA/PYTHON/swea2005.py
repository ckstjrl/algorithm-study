T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    arr[0][0] = 1
    for i in range(1, N):
        arr[i][0] = 1
        arr[i][i] = 1
    for j in range(2, N):
        for k in range(1, N):
            arr[j][k] = arr[j-1][k-1] + arr[j-1][k]
    print(f"#{test_case}")
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                print(arr[i][j], end=' ')
        print()