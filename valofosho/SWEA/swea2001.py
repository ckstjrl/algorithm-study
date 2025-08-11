T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_len = N-M+1
    max_sum = 0
    for i in range(max_len):
        for j in range(max_len):
            cur = 0
            # arr[i][j] # 좌상단끝점
            for mi in range(i,i+M):
                for mj in range(j,j+M):
                    cur += arr[mi][mj]
            if cur >= max_sum:
                max_sum = cur
            else:
                continue
    print(f"#{test_case} {max_sum}")