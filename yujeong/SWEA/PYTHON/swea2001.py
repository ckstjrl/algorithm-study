# swea 2001. 파리 퇴치 / D2

T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    # 영역별 파리 개수 
    flymap = [list(map(int, input().split())) for _ in range(N)]
    # 최대로 죽인 파리 수 
    max_kill = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for p in range(M):
                for q in range(M):
                    kill += flymap[i+p][j+q]

            if kill > max_kill:
                max_kill = kill

    print(f'#{t+1} {max_kill}')