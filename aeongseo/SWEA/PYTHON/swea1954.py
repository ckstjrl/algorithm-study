'''
1954. 달팽이 숫자
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]   # 값이 0인 N*N 배열 생성
    i, j = 0, 0                         # 인덱스
    cnt, idx = 1, 0                     # 배열 값, 방향 인덱스

    # print(arr)

    di = [0, 1, 0, -1]                  # i의 방향 (오, 아, 왼, 위)
    dj = [1, 0, -1, 0]                  # j의 방향 (오, 아, 왼, 위)

    # 시작점 : [0][0]에 1 대입
    arr[i][j] = cnt
    cnt += 1

    while cnt <= N*N:
        mi = i + di[idx]    # 방향에 따라 인덱스 증가 -> 임시 인덱스에 저장
        mj = j + dj[idx]

        if mi < N and mj < N and arr[mi][mj] == 0:  # 임시 인덱스가 배열의 인덱스를 넘지 않고, 값이 채워진 적이 없을 때
            i = mi                                  # i, j 에 임시 인덱스 저장
            j = mj
            arr[i][j] = cnt
            cnt += 1
        else:                                       
            idx = (idx + 1) % 4                     # 인덱스가 범위를 넘거나, 채워진 적이 있다면 방향 전환
    
    print(f'#{tc}')
    for lst in arr:
        print(*lst)
