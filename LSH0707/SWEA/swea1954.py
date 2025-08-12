T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)] # N * N
    start = 1 # 빈arr들르면서 start에 할당된 변수 추가하고 +1
    start_i = 0 # 오아왼위 한바퀴돌면 모든 시작점좌표가 00 --> 11(start_i를 1추가)
    def snail(start_i, N):
        global start
        if N < 1: # 종료조건 한바퀴돌때마다 상자크기가 가로세로2씩 작아짐
                  # 2 --> 0 아니면 1 --> -1 이면 종료
            return
        for i in range(N):
                arr[start_i][start_i+i] = start
                start = start + 1
        for i in range(1, N):
                arr[start_i+i][N-1+start_i] = start
                start = start + 1
        for i in range(N-2, -1, -1):
                arr[N-1+start_i][i+start_i] = start
                start = start + 1
        for i in range(N-2, 0, -1):
            arr[i+start_i][start_i] = start
            start = start + 1
        snail(start_i + 1, N - 2) 
        # 한바퀴돌고나면 시작점좌표(ex)00->11), N크기-2인 경우로 다시돌면됨
        # start는 global 변수로 둠
        
        
    snail(0, N)
    print(f'#{test_case}')
    for i in arr:
          print(*i)


    
    