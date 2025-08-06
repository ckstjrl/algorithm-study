T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N=전체 M=파리채
    arr = [list(map(int, input().split())) for _ in range(N)] # 전체판 [[],[],[]]
 
    max_M = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            max_2 = 0
            for p in range(i,i+M):
                for q in range(j,j+M):
                    max_2 = max_2 + arr[p][q]
            if max_M < max_2:
                max_M = max_2
    print(f'#{test_case} {max_M}')