# 파리 퇴치 / D2
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    kill_list = []
    for i in range(N-M+1): 
        for j in range(N-M+1):
    # M X M matrix의 [0][0] 인덱스가 놓이는 N X N의 인덱스 값
            kill = 0
            for r in range(M):
                for c in range(M):
                    kill += fly[i+r][j+c] # 죽인 파리 개수
            kill_list.append(kill)

    max_k = 0
    for k in kill_list:
        if max_k < k:
            max_k = k
    print(f'#{tc} {max_k}')