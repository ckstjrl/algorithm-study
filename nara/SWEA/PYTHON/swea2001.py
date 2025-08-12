T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            sum = 0
            for k in range(i, i + M):
                for l in range(j, j + M):
                    sum += arr[k][l]
            if sum > max:
                max = sum
    print(f"#{test_case} {max}")