# 1954. 달팽이 숫자 / D2

T = int(input())

for t in range(T):
    N = int(input())

    snail = [[0]*N for _ in range(N)] # 출력할 2차원 배열 초기화 
    num = 1
    idx = 0
    
    while num <= N**2:
        # case 1: 오른쪽으로
        for i in range(idx, N-idx):
            snail[idx][i] = num
            num += 1

        # case 2: 아래로
        for i in range(idx+1, N-idx):
            snail[i][N-idx-1] = num
            num += 1

        # case 3: 왼쪽으로
        for i in range(N-idx-2, idx-1, -1):
            snail[N-idx-1][i] = num
            num += 1

        # case 4: 위로 
        for i in range(N-idx-2, idx, -1):
            snail[i][idx] = num
            num += 1

        idx += 1
    
    print(f'#{t+1}')
    for s in snail:
        print(*s)