"""
풍선팡 보너스게임2
N * N 격자에 각 점수가 적힌 풍선이 존재
풍선을 터트리면 풍선이 위치한 행 및 열에 있는 모든 점수를 획득
하나의 풍선을 터트려서 얻을 수 있는 최대값을 출력
"""
# check를 함수로 만들어서 격자판 내부만 이동할 수 있도록 제한
def check(i,j,N):
    if 0<= i < N and 0<= j < N:
        return True
    else:
        return False
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 이동은 하 상 우 좌 순서
    # 순서는 크게 유의미하지 않음 
    di = [1, -1, 0 , 0]
    dj = [0, 0, 1, -1]
    max_sum = 0
    for i in range(N):
        for j in range(N):
            cen = arr[i][j]
            # 각각 모든 방향을 순회
            for d in range(4):
                # N-1 까지 곱해서 방향 이동 적용
                for c in range(1,N):
                    ni, nj = i+di[d]*c, j+dj[d]*c
                    if check(ni,nj, N):
                        cen += arr[ni][nj]
                    # 한 방향을 끝을 보고 오는 형식이므로 더이상 전진 불가능하면 break
                    else:
                        break
            if cen > max_sum:
                max_sum = cen
    print(f"#{test_case} {max_sum}")