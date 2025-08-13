T = int(input())
 
for tc in range(1, T+1):
    N, K = map(int, input().split())
 
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
 
    # 행 우선 순회
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:  # 칸의 값이 1이면 1의 개수를 1 증가
                cnt += 1
            else:               # 0이면 1의 개수를 0으로 초기화
                cnt = 0
            if cnt == K and (j == N-1 or arr[i][j+1] == 0):     # 1의 개수가 K이고, 칸의 위치가 행(열)의 마지막이거나 다음칸의 값이 0이면 자리 수 증가
                result += 1
        # print('col:', result)
 
    # 열 우선 순회
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                cnt = 0
            if cnt == K and (i == N-1 or arr[i+1][j] == 0):
                result += 1
        # print('row:', result)
 
    print(f'#{tc} {result}')