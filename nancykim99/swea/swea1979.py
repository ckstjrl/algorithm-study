T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    line_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1: # 가로로 K개 찾기
                cnt += 1
                if j == N-1 and cnt == K:
                    line_cnt += 1
            elif arr[i][j] == 0:
                if cnt == K:
                    line_cnt += 1
                cnt = 0
    
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1: # 세로로 K개 찾기
                cnt += 1
                if i == N-1 and cnt == K:
                    line_cnt += 1
            elif arr[i][j] == 0:
                if cnt == K:
                    line_cnt += 1
                cnt = 0

    
    print(f'#{tc} {line_cnt}')